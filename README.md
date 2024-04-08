# Alindor ML Engineer's Test Assignment

## Overview
A Flask-based application that leverages Deepgram for speech-to-text conversion and OpenAI for sentiment analysis, providing insights into dialogues. Hosted on the Google Cloud Platform, it's designed for scalability and insightful analysis of conversational sentiments.

## Features
- **Audio Upload**: Users can upload audio files for sentiment analysis.
- **Insightful Analysis**: Delivers deep psychological insights and sentiment analysis from dialogues.

## Challenges Faced
- **Speech to Text Diarization**: Ensuring each speaker was labelled separately required fine-tuning Deepgram's settings.
- **Sentiment Analysis Creativity**: Moving beyond generic sentiment analysis to provide insightful and specific psychological insights about the speakers involved significant experimentation with OpenAI's prompt engineering.
- **Scalability**: Designing a system that could efficiently scale to handle simultaneous uploads and analyses involved leveraging cloud technologies and optimizing our web interface.

## Quick Start
1. Clone the repository:
git clone https://github.com/donnedarnall/dialogue_sentiment_analysis.git && cd dialogue_sentiment_analysis

2. Install dependencies:
pip install -r requirements.txt

3. Set environment variables in `.env` for `DG_API_KEY` and `OPENAI_API_KEY`.
4. Run the Flask app:
python3 app.py

Access the app at `http://127.0.0.1:5001`.

## Usage
Through the web interface, upload an audio file to receive sentiment analysis and psychological insights about the conversation.

## Contact
- **Email**: donnedarnall@gmail.com
- **Project Link**: [https://github.com/donnedarnall/dialogue_sentiment_analysis](https://github.com/donnedarnall/dialogue_sentiment_analysis)

## Run it locally

docker run -d -p 80:8080 -e OPENAI_API_KEY=<Your api key> test
