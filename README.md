# Mental Health Chatbot

## Overview
This chatbot is designed to provide emotional support by analyzing user messages using sentiment analysis. Based on the detected sentiment, it responds with encouraging messages and suggests mental health resources when needed.

## Features
- **Sentiment Analysis:** Uses NLTK's Vader SentimentIntensityAnalyzer to determine if a message is positive, neutral, or negative.
- **Personalized Responses:** Offers different responses based on sentiment.
- **Mental Health Resources:** Provides links to mental health support when detecting negative sentiment.
- **Randomized Replies:** Ensures varied interactions for a more natural experience.

## Installation
### Prerequisites
Ensure you have Python installed (3.7+ recommended).

### Install Dependencies
Run the following command to install required libraries:
```bash
pip install nltk
```

## Usage
1. Run the chatbot script:
   ```bash
   python mental_health_chatbot.py
   ```
2. The chatbot will ask how you're feeling.
3. Based on your response, it will analyze the sentiment and provide a corresponding message.
4. If a negative sentiment is detected, it will suggest helpful mental health resources.
5. Type `exit`, `quit`, or `bye` to end the chat.

## Future Improvements
- Integration with voice recognition for better accessibility.
- AI-driven conversation flow for more meaningful interactions.
- Web or mobile app version for broader usability.
