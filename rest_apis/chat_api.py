from flask import request, Blueprint, jsonify
from Service.ChatGPTResponse import generate 
from Service.CreateSummaryFromPDF import custom_summary
# from app import app
import os
from Service.CreateDocFromPDF import CreateDoc
import json

chat_gpt_api = Blueprint('chat_gpt_api', __name__)

@chat_gpt_api.route("/chat")
def returnChatPrompt():
    data = request.get_json(force=True)
    prompt = data.get('prompt')
    return generate(prompt)
    

@chat_gpt_api.route("/chat/upload", methods=["POST"])
def createDocResponse():
    if 'file' not in request.files:
        return jsonify({'error' : 'File Not Found'}), 500
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No Selected file'}), 500
    
    file.save(os.path.join("uploads", file.filename))

    theResponse = custom_summary(
        file.filename, 
        "Create a summary of this resume in 3 bullet points",
         "map_reduce",
         1
        )

    return theResponse




