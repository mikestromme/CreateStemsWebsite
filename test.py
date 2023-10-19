from pydub import AudioSegment
import os

def test_audio_conversion():
    # Set the paths to ffmpeg and ffprobe in your script
    os.environ["PATH"] += os.pathsep + "C:/ffmpeg/bin"
    AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
    AudioSegment.ffprobe   = "C:/ffmpeg/bin/ffprobe.exe"

    audio = AudioSegment.from_mp3("C:/Temp/Audio In/Gel - Collective Soul.mp3")
    audio.export("C:/Temp/Audio Out/test.wav", format='wav')

test_audio_conversion()
