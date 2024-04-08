# Analyzes interview transcripts for sentiment and psychological insights using OpenAI's GPT-3.5-turbo model, 
# focusing on the emotional state and motivations of each speaker without summarizing the content.

from openai import OpenAI # type: ignore
import openai
import os

# Retrieve OpenAI API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
api_key = os.environ.get("OPENAI_API_KEY")

def analyze_audio(transcript) :
    MODEL = "gpt-3.5-turbo"
    transcript_string = ''.join([str(item) for item in transcript])

    # Send request to OpenAI for sentiment and psychological analysis
    #response = client.chat.completions.create(
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is focused on sentiment and psychological insights " + 
            "of a conversation. You do not summarize the conversation. You communicate succinctly and use correct grammar."},
            {"role": "user", "content": "For the following transcript, answer these questions for each speaker, with proper" + 
            "grammar, in FULL sentences, WITHOUT summarizing the transcript. Present each speaker's analysis on a separate line with a line between them: " +
            "How is the speaker feeling? What specifically is most important to them? What specifically motivates them? What is their psychological state? " + 
            "How does each speaker feel about each other? What personality traits best describe them?  " +
            "Do not summarize the transcript. Transcript: " + transcript_string},
        ],
        temperature=0,
    )

    #Print sentiment analysis
    '''
    print("\n\nAnalysis: \n")
    print(response.choices[0].message.content)
    '''
    return response.choices[0].message.content









'''
# Request sentiment analysis from OpenAI's GPT model
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=transcript,
    max_tokens=50,
    temperature=0.5,
    stop=["\n"]
)

# Extract sentiment analysis result from the response
sentiment_text = response.choices[0].text.strip()

# Print sentiment analysis result
print(sentiment_text)
'''