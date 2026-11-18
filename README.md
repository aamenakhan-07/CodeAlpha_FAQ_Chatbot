Python FAQ Chatbot

A simple and interactive FAQ Chatbot developed using Python, Flask, and Natural Language Processing (NLP).

This chatbot is designed to answer frequently asked questions related to Python programming. It processes user questions, compares them with predefined FAQs, and returns the most relevant answer.

Features

- Interactive web-based chat interface.
- Answers frequently asked Python programming questions.
- Text preprocessing using NLTK.
- Tokenization and stemming.
- Cosine similarity for matching user questions with stored FAQs.
- Displays a fallback message when no relevant answer is found.
- Clear Chat option to reset the conversation.

Technologies Used

- Python
- Flask
- NLTK
- HTML
- CSS
- JavaScript

Project Structure

CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── chatbot.py
├── faq_data.py
├── test_chatbot.py
├── requirements.txt
└── README.md

Installation

1. Clone this repository:

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder:

cd CodeAlpha_FAQ_Chatbot

3. Install the required libraries:

pip install -r requirements.txt

How to Run

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000

How It Works

1. The user enters a question through the chatbot interface.
2. The question is preprocessed using NLTK.
3. Tokenization and stemming are applied to the text.
4. Cosine similarity is calculated between the user's question and stored FAQ questions.
5. The chatbot selects the answer with the highest similarity score.
6. If the similarity score is below the defined threshold, a fallback message is displayed.

Testing

The project also includes "test_chatbot.py" to test chatbot responses through the terminal.

Project Objective

The objective of this project is to develop a basic FAQ chatbot that uses Natural Language Processing techniques to understand user questions and provide relevant answers.

Internship

Developed as part of the CodeAlpha Artificial Intelligence Internship.