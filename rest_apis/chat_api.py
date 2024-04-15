from flask import request, Blueprint, jsonify
from Service.ChatGPTResponse import generate
from Service.CreateSummaryFromPDF import custom_summary
# from app import app
import os
from Service.CreateDocFromPDF import CreateDoc
import json

chat_gpt_api = Blueprint('chat_gpt_api', __name__)


@chat_gpt_api.route("/chat", methods=["POST"])
def returnChatPrompt():
    data = request.get_json(force=True)
    prompt = data.get('prompt')
    return generate(prompt)


@chat_gpt_api.route("/chat/upload", methods=["POST"])
def createDocResponse():

    print("Inside Create Doc Function")

    if 'file' not in request.files:
        return jsonify({'error': 'File Not Found'}), 500

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No Selected file'}), 500

    file.save(os.path.join("uploads", file.filename))

    prompt = json.loads(request.form.get('prompt'))

    theResponse = custom_summary(
        file.filename,
        prompt,
        "map_reduce",
        1
    )

    return theResponse
