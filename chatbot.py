
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer

from faq_data import faqs

tokenizer = RegexpTokenizer(r'\w+')
stemmer = PorterStemmer()

stop_words = {
    "is", "am", "are", "the", "a", "an", "what",
    "who", "how", "in", "of", "to", "and", "do",
    "does", "for", "it", "this", "that", "can",
    "i", "you", "me", "my", "your", "tell"
}


def preprocess(text):
    words = tokenizer.tokenize(text.lower())

    cleaned_words = []

    for word in words:
        if word not in stop_words:
            cleaned_words.append(stemmer.stem(word))

    return cleaned_words


def calculate_similarity(words1, words2):
    all_words = set(words1 + words2)

    if not all_words:
        return 0

    vector1 = [words1.count(word) for word in all_words]
    vector2 = [words2.count(word) for word in all_words]

    dot_product = sum(
        a * b for a, b in zip(vector1, vector2)
    )

    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(b * b for b in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


def get_answer(user_question):
    user_words = preprocess(user_question)

    best_score = 0
    best_answer = None

    for faq in faqs:
        faq_words = preprocess(faq["question"])

        score = calculate_similarity(
            user_words, faq_words
        )

        if score > best_score:
            best_score = score
            best_answer = faq["answer"]

    if best_score < 0.60:
        return "Sorry, I couldn't find a relevant answer. Please try another question."

    return best_answer
