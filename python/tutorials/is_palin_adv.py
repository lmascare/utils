#!/usr/bin/python3

import scrabble

longest = ""

for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest = word
print(longest)
