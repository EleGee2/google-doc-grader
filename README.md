# Google Doc Grader

Google Doc Grader is a web application that allows users to submit a Google Doc link and receive a grade for the content of the document. The app uses the Google Docs API to access the content of the document and the OpenAI API to process it using GPT-4.

## Installation
To run Google Doc Grader, you'll need to have Python 3 installed on your system or virtual environment. You'll also need to install the following Python packages:

- Flask
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- openai

## Usage

To use Google Doc Grader, first start the Flask server:

`` run flask --app openapi run --debug``

Then navigate to `http://localhost:5000`in your web browser. You should see a form where you can submit a Google Doc link.

After submitting the link, the app will retrieve the content of the document using the Google Docs API and send it to the OpenAI API for processing with GPT-4. The app will then display the grading information to the user.


## Authentication
To access the Google Docs API and the OpenAI API, you'll need to set up authentication credentials for your application. Follow the instructions in the following links to set up authentication:

- [Google Docs API Authentication] (URL "https://developers.google.com/docs/api/quickstart/python#step_1_turn_on_the_api_name")
- [OpenAI API Authentication] (URL "https://beta.openai.com/docs/authentication")

Store your google credentials in the token.json file