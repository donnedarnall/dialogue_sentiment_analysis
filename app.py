# This Flask app enables users to upload audio files, which it then transcribes and analyzes for sentiment, 
# displaying the sentiment analysis results on the web interface.

from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField
import os 
from sentiment_analysis import analyze_audio
from audio_transcription import transcribe_audio

'''
import logging
import ssl

import http.client

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

#logging.basicConfig(level=logging.DEBUG)
#ssl._create_default_https_context = ssl._create_unverified_context

'''

app = Flask(__name__)
#api = Api(app)

#argument parsing
#parser = reqparse.RequestParser()
#parser.add_argument('q', help='Upload a dialogue file to analyse')

# Set the Flask secret key and upload folder
app.config['SECRET_KEY'] = 'f9bd6e772acc427f555546efb424054a'
app.config['UPLOAD_FOLDER'] = 'upload_folder'  


class AudioForm(FlaskForm):
    audio_file = FileField('Audio File', validators=[FileRequired()])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])



def upload_audio():

    form = AudioForm()
    if form.validate_on_submit():
        audio_file = form.audio_file.data
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'audio_file')

        # Save the uploaded file to the server
        audio_file.save(filename)  

        # Transcribe the audio file then analyze for sentiment analysis
        transcript = transcribe_audio(filename)
        audio_analysis = analyze_audio(transcript)

        return render_template('result.html', text_output=audio_analysis)
    return render_template('upload.html', form=form)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
