from flask import Flask, request, send_from_directory, render_template, url_for
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/mikes/Documents/Development/Python/CreateStemsWebsite/input_test'  # set this to your upload directory

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded file to the specified folder
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Define the command to run on the uploaded files
        command = f'demucs -n mdx_extra {filename}'

        try:
            # Run the command asynchronously
            process = subprocess.Popen(command, shell=True)
            process.wait()  # Wait for the command to finish

            # Provide a link for the user to download the result
            return f'<a href="C:/Users/mikes/Documents/Development/Python/CreateStemsWebsite/separated/mdx_extra_q/Barracuda">Download Result</a>'
        except Exception as e:
            return f"Error running command: {str(e)}"
        
@app.route('/C:/Users/mikes/Documents/Development/Python/CreateStemsWebsite/separated/mdx_extra_q/Barracuda', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
