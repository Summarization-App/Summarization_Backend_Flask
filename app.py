from flask import Flask, request, Response, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

from rest_apis.chat_api import chat_gpt_api
from rest_apis.health import health
# from langchain_openai import ChatOpenAI
# from langchain.schema import HumanMessage

app = Flask(__name__)

load_dotenv()

app.register_blueprint(chat_gpt_api)
app.register_blueprint(health)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder for Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/upload_file', methods=['POST'])
# def upload_file():

#     if 'file' not in request.files:
#         return jsonify({'error': 'No File found'})

#     file = request.files['file']

#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})

#     # Let us save the file location for now in local folder. Later we need to change it to AWS S3

#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

#     return jsonify({'message': 'Successfully uploaded file'})


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5100)


''' Test CURL
curl -XPOST localhost:5100
'''
