from PIL import Image, ImageDraw

texts = ["Scene 1", "Scene 2", "Scene 3"]

for i, text in enumerate(texts, 1):
    img = Image.new("RGB", (1280, 720), color=(30, 30, 30))
    d = ImageDraw.Draw(img)
    d.text((100, 100), text, fill=(255, 255, 255))
    img.save(f"output/images/scene_{i}.png")

print("Images created.")
