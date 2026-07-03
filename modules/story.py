import os

def save_story(story):

    os.makedirs("output", exist_ok=True)

    with open("output/story.txt", "w", encoding="utf-8") as f:
        f.write(story)

    return "output/story.txt"


def load_story():

    with open("output/story.txt", "r", encoding="utf-8") as f:
        return f.read()
