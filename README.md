
# Academia AI Assistant

## Project Overview
The **Academia AI Assistant** is an advanced web-based educational tool designed to create interactive, engaging, and personalized learning experiences across a wide range of subjects. Powered by OpenAI's latest GPT models, the platform answers questions, explains complex concepts, and provides step-by-step guidance in topics such as mathematics, science, history, and more. The assistant enhances learning through **visual aids**, utilizing the DALL·E API to generate diagrams, charts, and infographics to complement its text-based explanations.

---

## Key Features

### 1. Interactive Chatbot
- **Natural Conversations**: Engage in meaningful interactions to ask questions about various subjects like math, science, and history.
- **Personalized Learning**: Responses are tailored to the user’s knowledge level, offering simplified explanations for beginners or advanced insights for experienced learners.

### 2. Dynamic Image Generation
- **Visual Aids**: Automatically generates relevant images (e.g., diagrams, charts, infographics) to enhance understanding.
- **Enhanced Clarity**: Visual aids explain complex topics, such as molecular structures, historical timelines, or geometric proofs, with clarity.

### 3. Advanced Natural Language Processing (NLP)
- **Contextual Understanding**: Leverages GPT-4 to interpret queries and provide accurate, contextually relevant answers.
- **Step-by-Step Guidance**: Breaks down challenging problems, such as algebra or calculus equations, into manageable steps for better comprehension.

### 4. Multi-Topic Support
- **Wide Range of Subjects**: Covers mathematics (algebra, geometry, calculus), science (biology, chemistry, physics), history (events, civilizations, influential figures), and more.
- **Cross-Disciplinary Learning**: Offers insights that span multiple fields for a holistic educational experience.

### 5. Learning History and Progression
- **Track Progress**: Maintains a record of user interactions to provide progression-based responses.
- **Reinforced Learning**: Builds on previously learned concepts while addressing new topics as users advance.

---

## How It Works

1. **User Input**:
   - The user submits a query (e.g., "What is the Pythagorean Theorem?" or "Explain photosynthesis").

2. **Response Generation**:
   - GPT-4 processes the input, delivering a detailed and informative response.

3. **Image Generation**:
   - A secondary model determines if a visual aid would enhance the explanation and triggers the DALL·E API to create the image.

4. **Final Output**:
   - The chatbot provides a combined response: a text-based explanation accompanied by generated visuals for a richer learning experience.

---

## Prerequisites

Before starting the project, ensure the following:

- **Python 3.x** installed.
- **OpenAI API key** for GPT-4 and DALL·E integration.
- **Pip** (Python package installer) installed.
- Basic knowledge of HTML, CSS, and JavaScript for frontend customization.

---

## Setup Instructions

### 1. Create a Virtual Environment (Recommended):
- In your project directory, create a virtual environment:
  ```bash
  python3 -m venv venv
  ```
- Activate the virtual environment:
  - **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - **Mac/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 2. Install Dependencies:
- Install required packages using `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Set Up Environment Variables:
- In your project directory, create a `.env` file and add the following:
  ```plaintext
  OPENAI_API_KEY=your_openai_api_key
  ```

### 4. Install the Project Package:
- Use the following command to install the project package:
  ```bash
  python setup.py install
  ```

### 5. Run the Application:
- Start the chatbot application:
  ```bash
  python app.py
  ```

### 6. Interact with the Chatbot:
- Open your browser and go to:
  ```
  http://127.0.0.1:8000/
  ```
- Ask questions such as:
  - "What is the Pythagorean Theorem?"
  - "Explain the process of photosynthesis."
  - "Tell me about Ancient Egypt."
  - "Help me solve this math problem."

---

## Troubleshooting

### 1. Missing Environment Variables:
- Ensure the `OPENAI_API_KEY` is correctly set in your `.env` file.

### 2. Dependency Issues:
- Upgrade `pip` before reinstalling:
  ```bash
  pip install --upgrade pip
  ```

### 3. API Connectivity Issues:
- Verify your OpenAI API key is valid and active.

---

## Contributing

- Fork the repository to create your own version.
- Report bugs or issues you encounter.
- Submit pull requests for new features or improvements.

---

## Contact

For inquiries, feedback, or assistance, reach out via email:

**Email**: darklususnaturae@gmail.com