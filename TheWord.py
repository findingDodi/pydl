from TheWordGenerator import TheWordGenerator


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