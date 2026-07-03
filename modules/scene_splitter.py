def split_story(story):

    story = story.replace("\n", " ")

    parts = [s.strip() for s in story.split(".") if s.strip()]

    scenes = []

    for i, part in enumerate(parts):
        scenes.append({
            "scene": i + 1,
            "text": part + "."
        })

    return scenes
