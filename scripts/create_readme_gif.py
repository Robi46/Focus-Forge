from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
source = root / "docs" / "screenshots"
out = root / "docs" / "focusforge-overview.gif"
files = [source / "dashboard.png", source / "history.png", source / "notes.png", source / "focus-shield.png"]
labels = ["FOCUS DASHBOARD", "HISTORY ANALYTICS", "PRIVATE NOTES", "FOCUS SHIELD"]
frames = []
for path, label in zip(files, labels):
    image = Image.open(path).convert("RGB")
    image.thumbnail((420, 720), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (460, 790), "#F6FAF4")
    x = (canvas.width - image.width) // 2
    y = 42
    canvas.paste(image, (x, y))
    draw = ImageDraw.Draw(canvas)
    draw.text((20, 14), label, fill="#087A50")
    frames.append(canvas)
frames[0].save(out, save_all=True, append_images=frames[1:], duration=1500, loop=0, optimize=True)
print(out)
