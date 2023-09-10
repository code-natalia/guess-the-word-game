import random
from termcolor import colored

# stworzenie listy słów o określonej ilości liter


def input_word_len():
    while True:
        try:
            number_of_letters = int(input("Podaj ilość liter od 3 do 10: "))

            while number_of_letters not in range(0, 11):
                number_of_letters = int(input("Podaj ilość liter od 3 do 10: "))
        except:
            print("nie podano poprawnej ilości liter")
            continue
        return number_of_letters


def filter_words(opened_file, number_of_letters):
    words_in_game = []

    for line in opened_file:
        if len(line) == (number_of_letters + 1):
            words_in_game.append(line[:-1].upper())

    return words_in_game


def compute_frequency(word):
    letter_frequency = {}

    for letter in word:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1

    return letter_frequency


def guessing(words_in_game, word, number_of_letters):
    print("masz 6 prób aby odgadnąć słowo")

    for i in range(1, 11):
        print("to twoja " + str(i) + " próba")
        guess = input("podaj słowo = ").upper()

        while True:
            if guess in words_in_game:
                break
            print(colored("niepoprawne słowo", "red"))
            guess = input("podaj słowo = ").upper()

        letter_frequency = compute_frequency(word)

        for i in range(number_of_letters):
            if guess[i] == word[i]:
                letter_frequency[guess[i]] -= 1

        output = []

        if guess == word:
            print("Gratulacje!!! Hasło to: " + colored(word, "green"))
            exit()
        else:
            for i in range(number_of_letters):
                if guess[i] == word[i]:
                    output.append(colored(guess[i], "green"))
                elif letter_frequency.get(guess[i]) and letter_frequency[guess[i]] > 0:
                    output.append(colored(guess[i], "yellow"))
                    letter_frequency[guess[i]] -= 1
                else:
                    output.append(colored(guess[i], "white"))

            out = "".join(output)

            print(out)

    print("hasło to: " + word)


def game(words_in_game, word, number_of_letters):
    guessing(words_in_game, word, number_of_letters)
