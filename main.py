import os

# One image only: a library whose books argue endlessly.
LINE = "It is a library where every book argues with every other book, day and night, and the argument never ends."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
