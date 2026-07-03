from modules.scene_splitter import split_story

story = """
A boy entered a dark forest.
He found a glowing cave.
A dragon appeared.
The dragon gave him a magical crystal.
The boy became the guardian of the forest.
"""

scenes = split_story(story)

for s in scenes:
    print(s)
