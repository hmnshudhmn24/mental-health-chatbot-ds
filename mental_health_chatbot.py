import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import time
import random

# Download required data for sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Predefined responses based on sentiment
RESPONSES = {
    "positive": [
        "I'm glad to hear that! Keep up the positive mindset! 😊",
        "That sounds great! Stay happy and motivated!",
        "Your positivity is inspiring! Keep shining! 🌟"
    ],
    "neutral": [
        "I see. If you ever want to share more, I'm here to listen.",
        "Thanks for sharing. Let me know if you’d like to talk more.",
        "I appreciate you opening up. Take your time to express yourself."
    ],
    "negative": [
        "I'm sorry you're feeling this way. You're not alone. 💙",
        "It sounds like you're having a tough time. Would you like some resources for support?",
        "You're strong, and I believe in you. Would you like to try some relaxation techniques?"
    ]
}

# Mental health resources
RESOURCES = [
    "Here are some mental health helplines: https://www.mentalhealth.gov/",
    "You can try guided meditation here: https://www.headspace.com/",
    "Need support? Reach out to someone you trust or a mental health professional."
]

# Function to analyze sentiment
def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.2:
        return "positive"
    elif score <= -0.2:
        return "negative"
    else:
        return "neutral"

# Suggest mental health resources
def suggest_resources():
    return random.choice(RESOURCES)

# Chatbot loop
def chat():
    print("Hello! I'm your mental health chatbot. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Take care! Remember, you're not alone. 💙")
            break
        
        sentiment = analyze_sentiment(user_input)
        response = random.choice(RESPONSES[sentiment])  # Pick a random response
        print(f"Chatbot: {response}")
        
        if sentiment == "negative":
            print(f"Chatbot: {suggest_resources()}")
        
        time.sleep(1)

if __name__ == "__main__":
    chat()
