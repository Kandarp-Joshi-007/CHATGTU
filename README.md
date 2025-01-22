# CHATGTU
GTU specialized chatbot.**

*ChatGTU* is a chatbot designed specifically for Gujarat Technological University (GTU) students. It answers academic queries strictly within the GTU syllabus, ensuring accuracy and relevance. For queries beyond the syllabus, it provides a disclaimer and responds as a general-purpose chatbot.

---

## Features

- *Syllabus-Specific Answers*: Provides accurate and relevant responses based on GTU curriculum.
- *Disclaimer for Off-Syllabus Queries*: Clearly indicates when a query falls outside the GTU syllabus.
- *Interactive User Interface*: Allows users to select their semester and subject before querying.
- *Efficient Processing*: Prepares the chatbot in approximately 5 minutes for interaction.

---

## Technology Stack

- *Base LLM Models*: Llama 2, Phi 3
- *Frontend*: StreamLit
- *Backend*: Python

---

## System Architecture

1. *Knowledge Base*: Organized directory structure containing GTU syllabus materials:
   - *8 Semester Directories*: Each semester directory includes subject-specific materials.
   - *Official Resources*: Sourced from GTU-recognized materials and professors.
2. *Retrieval-Augmented Generation (RAG)*:
   - Retrieves relevant content from the knowledge base.
   - Converts data into embeddings and uses context for generating responses.
3. *Response Flow*:
   - User selects semester and subject.
   - The system processes and prepares for queries.
   - Queries are answered based on syllabus content or with a disclaimer for off-syllabus topics.

---

## Installation and Setup

1. *Clone the Repository*:
   bash
   git clone https://github.com/Kandarp-Joshi-007/ChatGTU.git
   cd ChatGTU
   

2. *Install Dependencies*:
   bash
   pip install -r requirements.txt
   

3. *Prepare Knowledge Base*:
   - Create a data directory in the root folder.
   - Organize GTU syllabus materials into semester and subject directories within data.

4. *Run the Application*:
   bash
   streamlit run app.py
   

5. *Access the Application*:
   - Open the provided URL in your browser to start using ChatGTU.

---

## User Workflow

1. Select your semester.
2. Choose the desired subject.
3. Ask any syllabus-related query.
4. If the query is off-syllabus, a disclaimer will be shown, followed by a general-purpose response.

---

## Future Enhancements

- Expand the knowledge base with additional GTU materials.
- Improve natural language understanding for complex queries.
- Add interactive features like study aids and tutorials.

---

## Contributing

We welcome contributions! Feel free to submit issues or pull requests for improvements and new features.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Gujarat Technological University (GTU)
- Darshan University for study material resources
- OpenAI for Llama 3.2 and Phi 3 models

---

## Contact

For queries or suggestions, feel free to contact us:
- Email: kandarpjoshi0809@gmail.com
- LinkedIn: https://www.linkedin.com/in/kandarp-joshi0809/
