# Automates audio transcription and speaker diarization using the Deepgram API,
# identifying and labeling different speakers in the transcription.

import requests
import os
from sentiment_analysis import analyze_audio
'''
import ssl
#import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLS)

session = requests.Session()
adapter = SSLAdapter()
session.mount('https://', adapter)

# Use session to make requests
#response = session.get('https://api.deepgram.com')
'''
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import certifi

#response = requests.get('https://api.deepgram.com', verify=certifi.where())


class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        # Create an SSL context with your specifications
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.options &= ~ssl.OP_NO_SSLv3
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        ssl_context.check_hostname = True
        ssl_context.load_default_certs()

        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_context=ssl_context,
                                       **pool_kwargs)

session = requests.Session()
adapter = SSLAdapter()
session.mount('https://', adapter)

# Now, use this session object to make your requests
# For example:
# response = session.get('https://api.deepgram.com/v1/listen', headers=headers, params=params, data=audio_file)

# Retrieve the Deepgram API key and set up the request headers for audio transcription.
api_key = os.getenv("DG_API_KEY")
headers = {
    'Authorization': f'Token {api_key}',
    'Content-Type': 'audio/mp3'
}

# Enable diarization
params = {
    'diarize': 'true',
    'diarize_version': 'latest',
}

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        response = requests.post('https://api.deepgram.com/v1/listen', headers=headers, params=params, data=audio_file)
        #response = requests.post('https://api.deepgram.com/v1/listen', headers=headers, params=params, data=audio_file, verify=False)
        #with requests.Session() as session:
         #   response = session.get('https://api.deepgram.com/v1/listen', headers=headers, params=params, data=audio_file, verify=certifi.where())

    transcript_lines = []

    # Check response
    if response.status_code == 200:
        data = response.json()

        current_speaker = None
        

        # Iterate through each word in the data
        for word in data['results']['channels'][0]['alternatives'][0]['words']:
            speaker_id = word['speaker']
            if speaker_id != current_speaker:
                # New speaker detected, switch speaker
                current_speaker = speaker_id
                transcript_lines.append((f"[Speaker_{speaker_id + 1}]", [word['word']]))
            else:
                # Same speaker as previous word, append word to the current line
                transcript_lines[-1][1].append(word['word'])

        # Print formatted transcript maintaining conversation order
    
        print("Transcription: \n")
        for speaker, words in transcript_lines:
            print(f"{speaker}: {' '.join(words)}")

               
 
    else:
        print("Error in transcription")
        print(response.text)

    return transcript_lines
