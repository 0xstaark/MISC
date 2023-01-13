#!/usr/bin/python3


import random
import requests


url_adjectives = 'https://raw.githubusercontent.com/0xstaark/test/main/adjectives.txt'

url_animals = 'https://raw.githubusercontent.com/0xstaark/test/main/animals.txt'

try:
    response_adjectives = requests.get(url_adjectives)
    adjectives = response_adjectives.text.split()

    response_animals = requests.get(url_animals)
    animals = response_animals.text.split()
except:
    print('Error: Unable to retrieve words from remote source')
    exit()

adjective = random.choice(adjectives)
animal = random.choice(animals)

newword = input('Would you like to generate a new word? (y/n): ')
while newword.lower() != 'n':
    adjective = random.choice(adjectives)
    animal = random.choice(animals)
    print(f'Your engagement name is: {adjective} {animal}\n')
    newword = input('Would you like to generate a new word? (y/n): ')
