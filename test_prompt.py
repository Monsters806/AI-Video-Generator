from modules.scene_splitter import split_story
from modules.image_prompt import create_prompts

story = """
A boy entered a magical forest.
He found an ancient temple.
A giant dragon appeared.
"""

scenes = split_story(story)
prompts = create_prompts(scenes)

for p in prompts:
    print(p)
