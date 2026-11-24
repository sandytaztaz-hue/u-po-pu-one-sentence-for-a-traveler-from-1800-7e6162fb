from pathlib import Path

TEXT = "It is a spider's web spun across the whole world, and a tug on one thread in London is felt 3,000 miles away in Boston in the time it takes to blink."

dest = Path("/output/entry.txt")
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(TEXT, encoding="utf-8")
print("chars:", len(TEXT))
