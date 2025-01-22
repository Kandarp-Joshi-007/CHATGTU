
import ollama
import streamlit as st
from openai import OpenAI
from utilities.icon import page_icon

st.set_page_config(
    page_title="Chat playground",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the models information.

    :param models_info: A dictionary containing the models' information.

    Return:
        A tuple containing the model names.
    """

    return tuple(model["name"] for model in models_info["models"])


def format_query_with_template(subject: str, question: str) -> str:
    """
    Formats the query using the provided template.

    :param subject: The subject related to the GTU syllabus.
    :param question: The user's question.
    :return: A formatted query string.
    """
    template = f"""
    # Your role

    You are a brilliant expert at understanding the intent of the questioner and the crux of the question, and providing the most optimal answer to the questioner's needs from GTU(Gujarat Technical University) based syllabus of {{subject}} only.

    # Instruction

    Your task is to answer the question using your own knowledge but only from GTU syllabus of {{subject}}


    # Constraint

    1. Think deeply and multiple times about the user's question
    User's question:
    {question}
    You must understand the intent of their question and provide the most appropriate answer.

    - Ask yourself why to understand the context of the question and why the questioner asked it, check if it is related to {{subject}}, and if it is, then provide an appropriate response based on what you understand.

    2. Choose the most relevant content(the GTU based content that directly relates to the question) and use it to generate an answer.

    3. Generate a concise, logical answer. 

    4. When the question does not relate to {{subject}} for the question or If you believe that question is out of the GTU syllabus, you should answer 'The Question asked is not relevant to {{subject}} in GTU'.

    # Question:

    {question}
    """.strip()
    return template.format(subject=subject, question=question)


def main():
    """
    The main function that runs the application.
    """

    page_icon("💬")
    st.subheader("Ollama Playground", divider="red", anchor=False)

    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    if available_models:
        selected_model = st.selectbox(
            "Pick a model available locally on your system ↓", available_models
        )

    else:
        st.warning("You have not pulled any model from Ollama yet!", icon="⚠️")
        if st.button("Go to settings to download a model"):
            st.page_switch("pages/03_⚙️_Settings.py")

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.text_area(label=message['role'], value=message['content'], height=200, key=message['role'] + str(message['time']))

    user_input = st.text_input("Enter your question here:")

    if st.button("Send"):
        if user_input:
            subject = "Artificial Intellegence"  # Replace with actual subject
            formatted_query = format_query_with_template(subject, user_input)

            response = client.completions.create(
                model=selected_model,
                prompt=formatted_query,
                max_tokens=1500,
            )

            st.session_state.messages.append({"role": "user", "content": user_input, "time": st.time()})
            st.session_state.messages.append({"role": "bot", "content": response.choices[0].text, "time": st.time()})
            st.experimental_rerun()

if __name__ == "__main__":
    main()
