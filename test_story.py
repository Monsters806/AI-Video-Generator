from modules.story import save_story, load_story

story = """
A boy discovered a hidden kingdom inside a mountain.
The kingdom had magical creatures and ancient secrets.
"""

save_story(story)

print(load_story())
