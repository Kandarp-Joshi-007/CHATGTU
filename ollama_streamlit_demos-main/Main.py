import ollama
import streamlit as st
from openai import OpenAI
from utilities.icon import page_icon

st.set_page_config(
    page_title="ChatGTU",
    page_icon="🎓",
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


def main():
    """
    The main function that runs the application.
    """

   # page_icon("🎓 ChatGTU")
    st.title("🎓 ChatGTU - GTU based Chatbot")

    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    if available_models:
        #selected_model = st.selectbox("Pick a model available locally on your system ↓", available_models)
        selected_model = "llama3.2"
        subjects = ["Artificial Intellegence", "Machine Learning", "Data Base Management System", "Software Engineering", "Basic Electrical Engineeering"]
        subject = st.selectbox("Choose the Subject",subjects)
    else:
        st.warning("You have not pulled any model from Ollama yet!", icon="⚠️")
        if st.button("Go to settings to download a model"):
            st.page_switch("pages/03_⚙️_Settings.py")

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter a prompt here..."):
        try:
            
            template = f"""
            # Your role

            You are a brilliant expert at understanding the intent of the questioner and the crux of the question, and providing the most optimal answer to the questioner's needs from GTU(Gujarat Technical University) based syllabus of {subject} only.

            # Instruction

            Your task is to answer the question using your own knowledge but only from GTU syllabus of {subject}


            # Constraint

            1. Think deeply and multiple times about the user's question
            User's question:
            {prompt}
            You must understand the intent of their question and provide the most appropriate answer.

            - Ask yourself why to understand the context of the question and why the questioner asked it, check if it is related to {subject}, and if it is, then provide an appropriate response based on what you understand.

            2. Choose the most relevant content(the GTU based content that directly relates to the question) and use it to generate an answer.

            3. Generate a concise, logical answer. 

            4. When the question does not relate to {subject} for the question or If you beleive that question is out of the GTU syllabus, you should answer 'The Question asked is not relevent to {subject} in GTU'.

            # Question:

            {prompt}
            """

            st.session_state.messages.append(
                {"role": "user", "content": prompt})

            message_container.chat_message("user", avatar="😎").markdown(prompt)

            with message_container.chat_message("assistant", avatar="🤖"):
                with st.spinner("model working..."):
                    stream = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": m["role"], "content": template}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )
                # stream response
                response = st.write_stream(stream)
            st.session_state.messages.append(
                {"role": "assistant", "content": response})

        except Exception as e:
            st.error(e, icon="⛔️")


if __name__ == "__main__":
    main()
