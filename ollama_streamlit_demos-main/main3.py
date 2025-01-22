import streamlit as st
import ollama

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit app layout
st.set_page_config(page_title="GTU Educational Chatbot", page_icon="🎓", layout="wide")
st.title("🎓 GTU Educational Chatbot")
st.write("Welcome to the GTU syllabus-based chatbot. Ask me anything related to your course subjects!")

st.sidebar.header("Select Subject")
subject = st.sidebar.selectbox(
    "Choose the subject related to your query:",
    ("Machine Learning", "Artificial Intelligence", "Data Structures", "Image Processing", "Database Management Systems")
)

st.write("### 🤖 Ask Your Question Below:")
question = st.text_input("Type your question here...")

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
        model='llama2',  # Assuming you're using a model called 'llama3.1'
        messages=[{'role': 'user', 'content': template}],
        stream=True,
    )

    response = ""
    for chunk in stream:
        response += chunk['message']['content']
    return response

if st.button("Get Answer"):
    if question:
        with st.spinner("Generating the best answer..."):
            response = generate_answer(subject, question)
            
            # Update the chat history
            st.session_state.chat_history.append({
                "question": question,
                "subject": subject,
                "response": response
            })

            st.success("Here is your answer:")
            st.write(f"**Question:** {question}")
            st.write(f"**Subject:** {subject}")
            st.write(f"**Answer:** {response}")
            st.balloons()  # Adds a fun balloon animation after getting the answer
    else:
        st.warning("Please enter a question before hitting the 'Get Answer' button.")

# Display the chat history
if st.session_state.chat_history:
    st.write("### 🗂️ Chat History")
    for chat in st.session_state.chat_history:
        st.write(f"**Question:** {chat['question']}")
        st.write(f"**Subject:** {chat['subject']}")
        st.write(f"**Answer:** {chat['response']}")
        st.write("---")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & Ollama")
