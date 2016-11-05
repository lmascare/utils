#!/usr/bin/python3

import scrabble

longest = ""

# word[::-1] means start from beginning to end with stride of -1
# -1 stride means go from back to front
# aka reverse of the word

for word in scrabble.wordlist:
  if word == word[::-1] and len(word) > len(longest):
        longest = word
print(longest)
