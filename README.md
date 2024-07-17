
# AI Content Generator


This project is an AI-powered content generation tool that leverages Hugging Face's models to create customized content based on user queries. The application is built using Streamlit and LangChain, providing an interactive UI for generating content tailored to different age groups and task types.

## Live Application

You can access the live application [here👉](https://huggingface.co/spaces/Visal9252/AI_Content_Generator).

## GitHub Repository

The source code for this project is available on GitHub: [AI-Content-Generator-Langchain-LLMS-Huggingface](https://github.com/vishal815/AI-Content-Generator-Langchain-LLMS-Huggingface).

## Features

- **Responsive UI**: The app features a visually appealing and responsive user interface.
- **Age-Specific Content**: Generate content tailored to Kids, Adults, or Senior Citizens.
- **Task-Specific Content**: Choose from various tasks like writing a sales copy, creating a tweet, writing a product description, or explaining a concept.
- **Customizable Word Limit**: Set the desired word limit for the generated content.

## Technologies Used

- **Streamlit**: For building the web application.
- **LangChain**: For creating the language model interface.
- **LLMs (Large Language Models)**: To process and generate human-like text.
- **Hugging Face**: For utilizing advanced AI models.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishal815/AI-Content-Generator-Langchain-LLMS-Huggingface.git
   cd AI-Content-Generator-Langchain-LLMS-Huggingface
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project directory.
   - Add your Hugging Face API token to the `.env` file:
     ```
     HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_token_here
     ```
     Replace `your_hugging_face_api_token_here` with your actual Hugging Face API token.

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Use the Application**:
   - Open your web browser and navigate to `http://localhost:8501`.
   - Enter your query in the text area.
   - Select the task you want to perform from the dropdown menu.
   - Select the target age group from the dropdown menu.
   - Adjust the word limit using the slider.
   - Click the "Generate Content" button to receive your customized content.

## Project Structure

- `app.py`: The main application file.
- `.env`: Environment variable file containing the Hugging Face API token.
- `requirements.txt`: List of dependencies required for the project.

## Vishal Lazrus

