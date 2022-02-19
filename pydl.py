# User-Eingaben außerhalb der Klasse
# Kontrolle innerhalb der Klasse
# TODO: BugFix Usereingabe Wortlänge
# TODO: BugFix Datei aufräumen (Zahlen und Sonderzeichen raus, Großbuchstaben in Kleinbuchstaben, etc)
import random


class TheWord:

    def __init__(self):
        my_word_generator = TheWordGenerator()
        self.word_to_find = my_word_generator.get_random_word()

    def get_word_len(self):
        return len(self.word_to_find)

    def is_word_correct(self, word):
        return word == self.word_to_find

    def word_check(self, word):
        compare_string = ""

        for i in range(len(word)):
            if word[i] == self.word_to_find[i]:
                compare_string += "o"
            elif word[i] in self.word_to_find:
                compare_string += "ø"
            else:
                compare_string += "x"

        return compare_string


class TheWordGenerator:

    def __init__(self):
        self.words = []
        self.read_words_from_file()

    def get_random_word(self):
        random_number = random.randrange(len(self.words))
        random_word = self.words[random_number]

        return random_word

    def read_words_from_file(self, filename="gpl.txt"):
        file_handle = open(filename, "r")
        file_content = file_handle.read()
        file_handle.close()
        words_from_file = file_content.split()

        self.words = words_from_file


class TheGame:

    def __init__(self):
        self.tries = 6

    def running_game(self):
        your_word = TheWord()

        print("The Word you are searching for has", your_word.get_word_len(), "letters!")
        print("o = Letter is on the correct position")
        print("ø = Letter is on the wrong position")
        print("x = Letter is not in the word")

        for i in range(self.tries):
            user_word = input("Enter Word: ")
            print(user_word)
            print(your_word.word_check(user_word))

            if not your_word.is_word_correct(user_word):
                if i < (self.tries - 1):
                    print("Try Again!")
                else:
                    print("You did not find the word", your_word.word_to_find)
            else:
                if i == 0:
                    print("Congrats! You won on the first try!")
                else:
                    print("Congrats! You won after", i + 1, "tries!")

                break


# Tests
#my_word = TheWord()
#print(my_word.word_check("pizza"))
#print(my_word.word_check("kampf"))
#print(my_word.word_check("holla"))
#print(my_word.word_check("hallo"))

my_game = TheGame()
my_game.running_game()
