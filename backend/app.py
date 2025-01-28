from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import requests
import os
import PyPDF2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = "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"


def extract_pdf_text(file_path):
    """Extract text from the uploaded PDF."""
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.strip()


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files['pdf']
    filename = secure_filename(pdf_file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    pdf_file.save(file_path)

    text_content = extract_pdf_text(file_path)
    if not text_content:
        return jsonify({"error": "Failed to extract text from PDF."}), 400

    query = request.form.get("query", "Summarize this document")

    # Query Groq API
    response = requests.post(
        GROQ_API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": f"{query}: {text_content[:2000]}"}
            ]
        }
    )
    result = response.json()
    answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")

    return jsonify({"answer": answer})
@app.route('/')
def home():
    return "Server is running. You can send requests to `/upload`."


if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, jsonify, request
# import PyPDF2
# import os
# import requests
#
# app = Flask(__name__)
# GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
# GROQ_API_KEY = "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"
#
# STATIC_PDF_PATH = os.path.join(app.static_folder, "NIPS-2017-attention-is-all-you-need-Paper.pdf")
#
# def extract_pdf_text(file_path):
#     """Extract text from the static PDF."""
#     text = ""
#     with open(file_path, "rb") as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             text += page.extract_text()
#     return text.strip()
#
# @app.route('/query_static', methods=['POST'])
# def query_static_pdf():
#     query = request.json.get("query")
#     if not query:
#         return jsonify({"error": "No query provided"}), 400
#
#     text_content = extract_pdf_text(STATIC_PDF_PATH)
#
#     # Call Groq API
#     response = requests.post(
#         GROQ_API_URL,
#         headers={"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_API_KEY}"},
#         json={
#             "model": "llama-3.3-70b-versatile",
#             "messages": [{"role": "user", "content": f"{query}: {text_content[:2000]}"}]
#         }
#     )
#     result = response.json()
#     answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
#
#     return jsonify({"answer": answer})
#
# if __name__ == '__main__':
#     app.run(debug=True)
