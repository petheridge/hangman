'''
Code to pull words from online list
'''

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.decode().splitlines()

textfile = open("hangman/words.txt", "w")
for element in WORDS:
    textfile.write(element + "\n")
textfile.close()
