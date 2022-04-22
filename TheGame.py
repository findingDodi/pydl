from TheWord import TheWord
import config


class TheGame:

    def __init__(self):
        self.tries = 6

    def print_guess_graph(self, guesses, word):
        print("*" * 10)
        print("Your guess graph for the word '", word, "'")
        print("\n".join(guesses))

    def get_stretched_word(self, word):
        stretched_word = ""
        # TODO: pythify
        for i in range(len(word)):
            stretched_word += word[i] + " "

        return stretched_word

    def running_game(self):
        print("Welcome to pydl!")
        your_word = TheWord()

        print("The Word you are searching for has", your_word.get_word_len(), "letters!")
        print(config.correct, "= Letter is on the correct position")
        print(config.wrong_place, "= Letter is on the wrong place")
        print(config.wrong, "= Letter is not in the word")

        for i in range(self.tries):
            print("You have", (self.tries - i), "left")
            user_word = input("Enter Word: ")
            if len(user_word) == your_word.get_word_len():
                print(self.get_stretched_word(user_word))
                print(your_word.word_check(user_word))

                if not your_word.is_word_correct(user_word):
                    if i < (self.tries - 1):
                        print("Try Again!")
                    else:
                        print("You did not find the word '", your_word.word_to_find, "'")
                        self.print_guess_graph(your_word.word_guesses, your_word.word_to_find)
                else:
                    if i == 0:
                        print("Congrats! You won on the first try!")
                        self.print_guess_graph(your_word.word_guesses, your_word.word_to_find)
                    else:
                        print("Congrats! You won after", i + 1, "tries!")
                        self.print_guess_graph(your_word.word_guesses, your_word.word_to_find)

                    break

            else:
                print("Your word must be", your_word.get_word_len(), "characters long!")
                print("Please try again!")
