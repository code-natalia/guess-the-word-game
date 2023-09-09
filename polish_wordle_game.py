import skrypt
import random

opened_file = open("słowa.txt", "r")

numbers_of_letters = skrypt.input_word_len()

words_in_game = skrypt.filter_words(opened_file, numbers_of_letters )

word = random.choice(words_in_game)

skrypt.game(words_in_game, word, numbers_of_letters)