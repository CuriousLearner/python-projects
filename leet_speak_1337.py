#! /usr/bin/env python


"""
chmod +x leet_speak_1337.py

python3 leet_speak_1337.py

./leet_speak_1337.py
"""

text = input("Please enter a text: ")

leet_speak_mapper = {
    "a": 4,
    "b": 8,
    "e": 3,
    "l": 1,
    "o": 0,
    "s": 5,
    "t": 7
}

for key, value in leet_speak_mapper.items():
    if key in text.lower():
        text = text.replace(key, str(value)).replace(key.upper(), str(value))

print("LeetSpeak output: ", text)
