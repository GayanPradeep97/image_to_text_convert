from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

# Set the path to the Tesseract executable if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return jsonify({'text': 'No image uploaded'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'text': 'No selected file'}), 400

    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    return jsonify({'text': text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
