import subprocess
import os

def generate_voice(text):

    os.makedirs("output", exist_ok=True)

    output_file = "output/audio.wav"

    subprocess.run([
        "espeak",
        "-w",
        output_file,
        text
    ], check=True)

    return output_file
