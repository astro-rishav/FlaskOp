from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from your_ml_module import classify_image  # Import your classification function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory to save uploaded files
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('classification.html')  # Render your classification page

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Process the image
        result = classify_image(file_path)  # Your image classification function
        
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid file type'})

if __name__ == '__main__':
    app.run(debug=True)
