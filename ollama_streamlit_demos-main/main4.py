import streamlit as st
import ollama

# Initialize session state for chat history and page switching
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "page" not in st.session_state:
    st.session_state.page = "Chat"

# Function to generate an answer using the Ollama model
def generate_answer(subject, question):
    template = f"""
    # Your role

    You are a brilliant expert at understanding the intent of the questioner and the crux of the question, and providing the most optimal answer to the questioner's needs from GTU(Gujarat Technical University) based syllabus of {subject} only.

    # Instruction

    Your task is to answer the question using your own knowledge but only from GTU syllabus of {subject}

    # Constraint

    1. Think deeply and multiple times about the user's question
    User's question:
    {question}
    You must understand the intent of their question and provide the most appropriate answer.

    - Ask yourself why to understand the context of the question and why the questioner asked it, check if it is related to {subject}, and if it is, then provide an appropriate response based on what you understand.

    2. Choose the most relevant content(the GTU based content that directly relates to the question) and use it to generate an answer.

    3. Generate a concise, logical answer. 

    4. When the question does not relate to {subject} for the question or If you believe that question is out of the GTU syllabus, you should answer 'The Question asked is not relevant to {subject} in GTU'.
    """

    stream = ollama.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': template}],
        stream=True,
    )

    response = ""
    for chunk in stream:
        response += chunk['message']['content']
    return response

# Sidebar for navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Go to Chat"):
    st.session_state.page = "Chat"

if st.sidebar.button("Go to Chat History"):
    st.session_state.page = "Chat History"

# Display the current page based on the session state
if st.session_state.page == "Chat":
    st.title("🎓 GTU Educational Chatbot")
    st.write("Welcome to the GTU syllabus-based chatbot. Ask me anything related to your course subjects!")

    subject = st.sidebar.selectbox(
        "Choose the subject related to your query:",
        ("Machine Learning", "Artificial Intelligence", "Data Structures", "Image Processing", "Database Management Systems")
    )

    st.write("### 🤖 Ask Your Question Below:")
    question = st.text_input("Type your question here and press Enter...", key="input")

    # If a question is entered, generate the response and update the chat history
    if question:
        with st.spinner("Generating the best answer..."):
            response = generate_answer(subject, question)
            st.session_state.chat_history.append({
                "question": question,
                "subject": subject,
                "response": response
            })
            # Clear the input box after submitting
            st.session_state.input = ""

    # Display the current chat in a chat-like format
    for chat in st.session_state.chat_history:
        st.write("---")
        st.markdown(f"**📩 You:** {chat['question']}")
        st.markdown(f"**📘 Subject:** {chat['subject']}")
        st.markdown(f"**🤖 Chatbot:** {chat['response']}")

elif st.session_state.page == "Chat History":
    st.title("🗂️ Chat History")
    st.write("Here you can see all your previous conversations.")

    # Display the chat history in a chat-like format
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            st.write("---")
            st.markdown(f"**📩 You:** {chat['question']}")
            st.markdown(f"**📘 Subject:** {chat['subject']}")
            st.markdown(f"**🤖 Chatbot:** {chat['response']}")
    else:
        st.write("No chat history available.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & Ollama")
