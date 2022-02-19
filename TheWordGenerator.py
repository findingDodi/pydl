import random


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