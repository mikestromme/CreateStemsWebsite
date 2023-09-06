import torch
from demucs import pretrained
import librosa
import os
from pathlib import Path

input_folder = Path('input')

# Load a pre-trained model
model = pretrained.load_pretrained('demucs')

# Load an audio file and resample it to 44100 Hz
audio, _ = librosa.load(input_folder/'Get Back.wav', sr=44100)

# Convert the audio data to a torch tensor
audio = torch.tensor(audio)

# Separate the audio into stems
with torch.no_grad():
    stems = model(audio)


# type this in once venv activated - demucs -n mdx_q "Get Back.mp3"
