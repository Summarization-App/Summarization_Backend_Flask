from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
# from langchain_openai import ChatOpenAI
# from langchain.schema import HumanMessage

app = Flask(__name__)

load_dotenv()

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder for Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@app.route('/', methods=["GET"])
def hello():
    def generate():
        stream = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello There!"}],
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield (chunk.choices[0].delta.content)

    return generate(), {"Content-Type": "text/plain"}


@app.route('/upload_file', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({'error': 'No File found'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Let us save the file location for now in local folder. Later we need to change it to AWS S3

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return jsonify({'message': 'Successfully uploaded file'})


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5100)


''' Test CURL
curl -XPOST localhost:5100
'''
