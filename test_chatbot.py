from chatbot import get_answer

print("===== Python FAQ Chatbot Test =====")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    answer = get_answer(question)

    print("Chatbot:", answer)