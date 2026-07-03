def create_prompts(scenes):

    prompts = []

    for scene in scenes:
        prompts.append({
            "scene": scene["scene"],
            "prompt": f"Cinematic, ultra detailed, 16:9, {scene['text']}"
        })

    return prompts
