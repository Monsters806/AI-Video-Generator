from modules.tts import generate_voice

story = """
Once upon a time, a young explorer found a hidden kingdom full of magic.
"""

file = generate_voice(story)

print("Voice saved:", file)
