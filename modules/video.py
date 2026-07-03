import subprocess

def create_video():

    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", "output/images/scene_1.png",
        "-i", "output/audio.wav",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "output/final.mp4"
    ]

    subprocess.run(command, check=True)

    return "output/final.mp4"
