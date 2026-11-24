"""One sentence explaining the modern internet to a traveler from 1800."""

import os

SENTENCE = "It is one great post office where a letter you post reaches the far side of the world before your tea cools, and a thousand strangers can write back before morning."

os.makedirs("/output", exist_ok=True)
# The gate allows 1 to 200 characters, no trailing newline.
assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(SENTENCE)
