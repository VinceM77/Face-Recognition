from flask import Flask, render_template, request, jsonify
from model.classifier import classify_image, load_saved_artifacts
import base64

app = Flask(__name__)

# Load saved artifacts (class dictionary and model)
load_saved_artifacts()

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'result': 'Aucun fichier sélectionné'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'result': 'Aucun fichier sélectionné'})

    if file:
        try:
            # Read the uploaded file as a base64-encoded string
            base64_data = base64.b64encode(file.read()).decode()

            # Perform image preprocessing
            preprocessed_data = base64_data  # No additional preprocessing needed

            # Perform image classification using the provided function
            result = classify_image(preprocessed_data)

            return render_template('index.html', result=result)
        except Exception as e:
            return jsonify({'result': f'Erreur : {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
