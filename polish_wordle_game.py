import helpers
import random

opened_file = open("polish_words.txt", "r")

numbers_of_letters = helpers.input_word_len()

words_in_game = helpers.filter_words(opened_file, numbers_of_letters)

word = random.choice(words_in_game)

helpers.game(words_in_game, word, numbers_of_letters)
