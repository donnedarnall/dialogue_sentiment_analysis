# Builds a Flask application image using Python 3.8 slim as a base.

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /dialogue_sentiment_analysis

# Copy the current directory contents into the container at /app
COPY . /dialogue_sentiment_analysis

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define environment variables for Flask to run
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080

ENV DEEPGRAM_RUN_PORT 443
# Ensure you replace 'your_secret_key_here' with your actual Flask secret key
ENV SECRET_KEY your_secret_key_here
ENV UPLOAD_FOLDER upload_folder

#ENTRYPOINT ["python3"]

# Command to run the Flask application
CMD ["python3", "app.py"]
#CMD ["flask", "run"]
