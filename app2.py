from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO
import subprocess
import threading

app = Flask(__name__)
socketio = SocketIO(app)

def run_demucs():
    process = subprocess.Popen(['demucs', '-n', 'mdx_extra', 'input/Barracuda.mp3'], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, 
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            # Parse the output to get progress information
            # Send progress back to the browser
            progress = subprocess.run(['demucs', '-n', 'mdx_extra', 'input/Barracuda.mp3'])  # Extract progress from output  # Extract progress from output
            print(progress)  # For testing, you can print it out
            socketio.emit('update_progress', {'progress': progress})

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/process', methods=['POST'])
def process_audio():
    # Start the background task to run the demucs command
    socketio.start_background_task(target=run_demucs)
    return 'Processing started'

if __name__ == '__main__':
    socketio.run(app, debug=True)
