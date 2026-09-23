from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "LegalEase Backend is running!"


@app.route("/generate", methods=["POST"])
def generate_document():
    data = request.get_json()

    document_type = data.get("document_type", "")
    details = data.get("details", "")

    if not document_type or not details:
        return jsonify({
            "error": "Document type and details are required."
        }), 400

    document = f"""
LEGAL DOCUMENT DRAFT

Document Type:
{document_type}

Details:
{details}

This document is an AI-assisted draft.
Please review the document and consult a qualified legal professional before using it for actual legal purposes.
"""

    return jsonify({
        "document": document.strip()
    })


if __name__ == "__main__":
    app.run(debug=True)s
