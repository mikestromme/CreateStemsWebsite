from spleeter.separator import Separator
from pydub import AudioSegment
from pathlib import Path
import tensorflow as tf 
import numpy as np
import os
import threading

# Disable TensorFlow multiprocessing
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)


def main():

    # Set the paths to ffmpeg and ffprobe in your script
    os.environ["PATH"] += os.pathsep + "C:/ffmpeg/bin"
    AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
    AudioSegment.ffprobe   = "C:/ffmpeg/bin/ffprobe.exe"


    input_folder = Path(f'C:/Users/mikes/Desktop/Create Stems Testing/Audio In/')
    output_folder = Path(f'C:/Users/mikes/Desktop/Create Stems Testing/Audio Out/spleeter')
    mp3_file = input_folder / 'Gel - Collective Soul.mp3'
    wav_file = input_folder / 'Gel - Collective Soul.wav'

    audio = AudioSegment.from_mp3(str(mp3_file))
    audio.export(str(wav_file), format='wav')
    

    input_file = input_folder / 'Gel - Collective Soul.wav'    

    separator = Separator('spleeter:4stems')
    separator.separate_to_file(str(input_file), str(output_folder))

    # Perform audio separation in a separate thread
    separate_thread = threading.Thread(target=separate_audio, args=(input_file, output_folder))
    separate_thread.start()
    separate_thread.join()

if __name__ == '__main__':
    # Add the freeze_support() call
    #from multiprocessing import freeze_support
    #freeze_support()

    main()
