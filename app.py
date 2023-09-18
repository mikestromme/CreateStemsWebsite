from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

import subprocess

@app.route('/process', methods=['POST'])
def process_audio():
    uploaded_file = request.files['file']
    uploaded_file.save('input/Barracuda.mp3')  # Save the uploaded file

    # Run the demucs command
    process = subprocess.Popen(['demucs', '-n', 'mdx_extra', 'input/Barracuda.mp3'], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
    
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            # Parse the output to get progress information
            # Update the progress bar using JavaScript
            progress = subprocess.run(['demucs', '-n', 'mdx_extra', 'input/Barracuda.mp3'])  # Extract progress from output
            print(progress)  # For testing, you can print it out
            
    return 'Processing complete'


if __name__ == '__main__':
    app.run(debug=True)


    
