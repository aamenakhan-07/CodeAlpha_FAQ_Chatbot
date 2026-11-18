
from flask import Flask, request, render_template_string
from chatbot import get_answer

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python FAQ Chatbot</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 30px auto;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #243b64;
        }

        .subtitle {
            text-align: center;
            color: #666;
        }

        .chat-box {
            background: #f5f7fb;
            padding: 15px;
            height: 350px;
            overflow-y: auto;
            border-radius: 10px;
            margin: 20px 0;
        }

        .message {
            padding: 12px;
            margin: 10px 0;
            border-radius: 10px;
            line-height: 1.5;
        }

        .user {
            background: #dce9ff;
            text-align: right;
        }

        .bot {
            background: #e3f5e8;
        }

        form {
            display: flex;
            gap: 8px;
        }

        input {
            flex: 1;
            min-width: 0;
            padding: 13px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 15px;
        }

        button {
            padding: 12px 18px;
            background: #315da8;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .clear {
            display: block;
            margin: 15px auto 0;
            background: #666;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Python FAQ Chatbot</h1>

    <p class="subtitle">
        Ask me anything about Python programming!
    </p>

    <div class="chat-box" id="chatBox">

        {% for item in history %}
            <div class="message user">
                <strong>You:</strong> {{ item.question }}
            </div>

            <div class="message bot">
                <strong>Chatbot:</strong> {{ item.answer }}
            </div>
        {% endfor %}

    </div>

    <form method="POST">
        <input
            type="text"
            name="question"
            placeholder="Type your question..."
            required
        >

        <button type="submit">Send</button>
    </form>

    <form method="POST" action="/clear">
        <button class="clear" type="submit">
            Clear Chat
        </button>
    </form>

</div>

<script>
    const chatBox = document.getElementById("chatBox");
    chatBox.scrollTop = chatBox.scrollHeight;
</script>

</body>
</html>
"""

chat_history = []


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            answer = get_answer(question)

            chat_history.append({
                "question": question,
                "answer": answer
            })

    return render_template_string(
        HTML_PAGE,
        history=chat_history
    )


@app.route("/clear", methods=["POST"])
def clear_chat():

    chat_history.clear()

    return render_template_string(
        HTML_PAGE,
        history=chat_history
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
