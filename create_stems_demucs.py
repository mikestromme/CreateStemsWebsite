from demucs import demucs
from pydub import AudioSegment
from pathlib import Path
import os
import threading

def separate_audio(input_file, output_folder):
    model = demucs()
    # Load the model weights
    model_path = os.path.join(output_folder, "demucs.th")
    model.load(model_path)

    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Separate the audio sources
    sources = model(audio)

    # Save the separated sources
    for i, source in enumerate(sources):
        source_path = os.path.join(output_folder, f"source_{i+1}.wav")
        source.export(source_path, format='wav')

def main():
    input_folder = Path('input')
    output_folder = Path('output')

    mp3_file = input_folder / 'Get Back.mp3'
    wav_file = input_folder / 'Get Back.wav'

    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')

    input_file = str(wav_file)
    output_folder = str(output_folder)

    separate_thread = threading.Thread(target=separate_audio, args=(input_file, output_folder))
    separate_thread.start()
    separate_thread.join()

if __name__ == '__main__':
    main()

""" testing:

demucs -n mdx_q myfile.mp3

demucs PATH_TO_AUDIO_FILE_1 [PATH_TO_AUDIO_FILE_2 ...]   # for Demucs
# If you used `pip install --user` you might need to replace demucs with python3 -m demucs
python3 -m demucs --mp3 --mp3-bitrate BITRATE PATH_TO_AUDIO_FILE_1  # output files saved as MP3
# If your filename contain spaces don't forget to quote it !!!
demucs "my music/my favorite track.mp3"
# You can select different models with `-n` mdx_q is the quantized model, smaller but maybe a bit less accurate.
demucs -n mdx_q myfile.mp3
# If you only want to separate vocals out of an audio, use `--two-stems=vocal` (You can also set to drums or bass)
demucs --two-stems=vocals myfile.mp3

demucs --two-stems=vocals "Get Back.mp3"

 """
