from TheWordGenerator import TheWordGenerator
import config


class TheWord:

    def __init__(self):
        my_word_generator = TheWordGenerator()
        self.word_to_find = my_word_generator.get_random_leveled_word()

    def get_word_len(self):
        return len(self.word_to_find)

    def is_word_correct(self, word):
        return word == self.word_to_find

    def word_check(self, word):
        compare_string = ""

        for i in range(len(word)):
            if word[i] == self.word_to_find[i]:
                compare_string += config.correct
            elif word[i] in self.word_to_find:
                compare_string += config.wrong_place
            else:
                compare_string += config.wrong

        return compare_string
