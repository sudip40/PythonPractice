import random

word_list = [
    "apple",
    "banana",
    "orange",
    "grape",
    "strawberry",
    "melon",
    "peach",
    "kiwi",
    "pineapple",
    "blueberry",
    "mango",
    "pear",
    "plum",
    "cherry",
    "raspberry",
    "apricot",
    "blackberry",
    "watermelon",
    "lemon",
    "lime"
]

random_number = random.randint(0, 20)
random_word = word_list[random_number]
print(random_word)

# TODO as the user to guess the letter and assign their ans to a variable called guess. Make guess lowercase.

# TODO check if the guessed letter is one of the choosen word's letter or not
