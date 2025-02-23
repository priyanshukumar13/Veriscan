import os
import hashlib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 10 * 1024 * 1024

suspicious_extensions = ['.exe', '.dll', '.bat', '.scr', '.vbs']

known_malicious_hashes = [
    "15e029c3834435150c76741e714540fcb799662db8cc2c61ba4ef192a781727b",  
    "2c464648ff97fd39dab054d0c3e1bd249e244fcc975b697e312796669c7763f1",
    "2c464648ff97fd39dab054d0c3e1bd249e244fcc975b697e312796669c7763f1",
    "3e1fb4ff54112a78d8bdccbe596c119201f079010c4f69cdf2c99385e7aee3dc",
    "43670ae43df9e361fa15f09f611da32db104ee207ed5af3e7e7f098ad82a68e0",
    "47f1570e770d236836c0d3cb50755b6dd91e1be58a0d3e61507c7baacfd27784",
    "5b0ba8d58a64630cb5fcb80e72520bd2ef6f322003fa2588d4d594620e6685ae",
    "7b98cd3800dede6537cf78e7b61eeeda71d251dc97c70cb7c2135c6aa310ab7f",
    "d150feb631d6e9050b7fb76db57504e6dcc2715fe03e45db095f50d56a9495a5",
    "d56bb81d0f8e4de24dc12a7d963ed95eec36291c71a29d6b434e72f098cc1131",
    "da26ba1e13ce4702bd5154789ce1a699ba206c12021d9823380febd795f5b002",
    "e4e5c3a6c15beff4e17117075e2c0bd65f176d81e6885134d2b4d97c20d4773a",
    "f681c1f8c12956a20c27beb9be1112374fefc7651884d7dd92010b40db1e7bee",
    "f7b0d6d95f2644e32c22eb3e681e33387ac27d71dd73eee3ff37ce77985ab177",
]

def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def get_file_size(file_path):
    return os.path.getsize(file_path)

def check_file(file_path):
    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_name)[1].lower()
    file_size = get_file_size(file_path)
    file_hash = get_file_hash(file_path)

    if file_size > MAX_FILE_SIZE:
        return {"status": "suspicious", "message": f"File too large: {file_name}. Maximum size allowed is 10MB.", "file_size": file_size}

    if file_ext in suspicious_extensions:
        return {"status": "suspicious", "message": f"Suspicious file extension detected: {file_name} Unsafe", "file_size": file_size}

    if file_hash in known_malicious_hashes:
        return {"status": "suspicious", "message": f"Malicious file detected : {file_name} Unsafe", "file_size": file_size}

    return {"status": "clean", "message": "File is clean. Safe", "file_size": file_size}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = check_file(file_path)

    file_size_in_mb = result['file_size'] / (1024 * 1024)
    result['file_size'] = f"{file_size_in_mb:.2f} MB"

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
