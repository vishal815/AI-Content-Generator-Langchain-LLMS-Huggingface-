import streamlit as st
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

def getLLMResponse(query, age_option, tasktype_option):

    if age_option == "Kid":
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
            },
            {
                "query": "Why is the sky blue?",
                "answer": "The sky is blue because it wears its favorite color, just like you might have a favorite t-shirt!"
            },
            {
                "query": "How do birds fly?",
                "answer": "Birds fly by flapping their wings, which are like tiny airplane wings, lifting them up into the sky for a grand adventure!"
            }
        ]
    elif age_option == "Adult":
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile is a portable communication device, commonly known as a mobile phone or cell phone. It allows users to make calls, send messages, access the internet, and use various applications. Additionally, 'mobile' can also refer to a type of kinetic sculpture that hangs and moves in the air, often found in art installations or as decorative pieces."
            },
            {
                "query": "Why is the sky blue?",
                "answer": "The sky appears blue because molecules in the air scatter blue light from the sun more than they scatter red light. This scattering causes the blue hue we see during the day."
            },
            {
                "query": "How do birds fly?",
                "answer": "Birds fly by using their wings, which provide lift and thrust. The shape of the wings and the way they move allow birds to generate the necessary aerodynamic forces to stay airborne."
            }
        ]
    elif age_option == "Senior Citizen":
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile, also known as a cellphone or smartphone, is a portable device that allows you to make calls, send messages, take pictures, browse the internet, and do many other things. In the last 50 years, I have seen mobiles become smaller, more powerful, and capable of amazing things like video calls and accessing information instantly."
            },
            {
                "query": "Why is the sky blue?",
                "answer": "The sky appears blue due to the scattering of sunlight by the atmosphere. This phenomenon, known as Rayleigh scattering, affects the shorter wavelengths of light, such as blue, more than the longer wavelengths."
            },
            {
                "query": "How do birds fly?",
                "answer": "Birds fly by flapping their wings to create lift and thrust. Over the years, I've observed how their feathers and wing shapes have adapted perfectly to aid their flight."
            }
        ]

    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )

    prefix = """You are helping a {template_ageoption}. Task: {template_tasktype_option}.
    Here are some examples:
    """

    suffix = """
    Question: {template_userInput}
    Response: """

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )

    new_prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["template_userInput", "template_ageoption", "template_tasktype_option"],
        example_separator="\n"
    )

    prompt = new_prompt_template.format(
        template_userInput=query,
        template_ageoption=age_option,
        template_tasktype_option=tasktype_option
    )

    print("---- PROMPT SENT TO MODEL ----")
    print(prompt)

    # Direct InferenceClient call — no LangChain HF wrapper, no .post() issue
    client = InferenceClient(
        model="google/flan-t5-large",
        token=os.getenv('HUGGINGFACEHUB_API_TOKEN')
    )

    response = client.text_generation(
        prompt=prompt,
        max_new_tokens=256,
        temperature=0.7,
    )

    print("---- MODEL RESPONSE ----")
    print(response)

    return response


# ── UI ──────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Content Generator",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("AI-Powered Content Creation")

form_input = st.text_area('Type your query here...', height=150)

tasktype_option = st.selectbox(
    'Select the task you want to perform:',
    ('Write a sales copy', 'Create a tweet', 'Write a product description', 'Explain a concept'),
    key=1
)

age_option = st.selectbox(
    'Select the target age group:',
    ('Kid', 'Adult', 'Senior Citizen'),
    key=2
)

numberOfWords = st.slider('Word limit:', 1, 200, 50)

submit = st.button("Generate Content")

if submit:
    if not form_input.strip():
        st.warning("Please type a query first.")
    else:
        with st.spinner('Generating content...'):
            try:
                response = getLLMResponse(form_input, age_option, tasktype_option)
                st.success("Content generated successfully!")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
