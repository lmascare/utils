#!/usr/bin/python3

import scrabble

longest = ""

for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
           is_palindrome = False

    if is_palindrome and len(word) > len(longest):
        longest = word
print(longest)
