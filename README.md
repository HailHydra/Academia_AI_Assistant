
Academia AI Assistant

Project Overview:
The Learning Chatbot is a web-based application designed to provide educational assistance by answering questions and explaining complex concepts in an easy-to-understand manner. It uses OpenAI’s latest GPT model for conversational interaction and offers users a dynamic learning experience across various topics, including mathematics, science, and history. The chatbot generates detailed step-by-step explanations, visual aids, and personalized feedback based on user inputs.

---

Features:

1. Interactive Chatbot:
   - Engage in natural conversations with the chatbot to ask questions and receive educational content across a wide range of subjects.

2. Image Generation (via Secondary GPT Model):
   - A secondary GPT model detects when an answer would benefit from a visual representation, such as diagrams, charts, or other educational images.
   - When necessary, the chatbot triggers the DALL·E API to generate relevant images, which are incorporated into the conversation to enhance understanding.

3. Natural Language Processing (NLP):
   - The chatbot uses GPT-4 to understand and respond to a variety of educational queries, delivering relevant and accurate answers.

4. Step-by-Step Explanations:
   - For complex topics, especially in subjects like mathematics and science, the chatbot provides detailed, step-by-step breakdowns and explanations to make learning easier.

5. Multi-Topic Learning:
   - Covers a variety of subjects including mathematics (algebra, geometry, calculus), science (biology, chemistry, physics), and history (historical events, civilizations, important figures).

6. Personalized Responses:
   - The chatbot tailors responses to the user's input, simplifying explanations for beginners or providing extra details for advanced learners.

---

How It Works:
1. User Input: The user asks a question about a specific topic (e.g., "What is the Pythagorean Theorem?" or "Explain photosynthesis").
2. Response Generation: The primary GPT-4 model processes the input and generates an initial response.
3. Image Detection: A secondary GPT model analyzes the response to determine if a visual aid (chart, diagram, etc.) would improve the explanation.
4. Image Generation: If needed, the chatbot triggers the DALL·E API to create an image relevant to the explanation.
5. Final Output: The chatbot delivers both the text response and any generated images to the user for a richer learning experience.

---

Prerequisites:

Before running the project, ensure the following requirements are met:
- Python 3.x installed.
- OpenAI API key (for GPT integration).
- Your machine should have pip (Python package installer) installed.
- Basic knowledge of HTML, CSS, and JavaScript for frontend customization.

---

Steps to Set Up:

1. Create a Virtual Environment (Optional but Recommended):
   Navigate to your project directory in the terminal/command prompt and create a new virtual environment:
   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

2. Install Required Dependencies:
   Once the virtual environment is activated, install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set Up Environment Variables:
   Create a .env file in your project directory and add the following line:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Install the Package:
   Install the necessary package with:
   ```bash
   python setup.py install
   ```

5. Run the Application:
   After setting up everything, run the application with the following command:
   ```bash
   python app.py
   ```

6. Interact with the Chatbot:
   Once the app is running, navigate to http://127.0.0.1:5000/ in your web browser. You’ll be able to interact with the chatbot, asking questions such as:
   - "What is the Pythagorean Theorem?"
   - "Explain how photosynthesis works."
   - "Tell me about the history of Ancient Egypt."
   - "Help me solve this math problem."

   The chatbot will guide you through the entire learning process.

---

Troubleshooting:
- Missing Environment Variables: Ensure the OPENAI_API_KEY is correctly set in your .env file.
- Dependencies: If any dependencies fail to install, try running the following before installing again:
  ```bash
  pip install --upgrade pip
  ```
- API Issues: If you encounter issues related to OpenAI API, double-check your OPENAI_API_KEY and ensure it’s valid and active.

---

Contribution:
Feel free to fork the repository, report issues, and submit pull requests. Contributions are welcome!

---

Contact:
For any issues or inquiries, contact the author at:

Email: darklususnaturae@gmail.com