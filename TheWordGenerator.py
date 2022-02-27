from TheLevel import TheLevel
import random
import re


class TheWordGenerator:

    def __init__(self):
        self.words = []
        self.read_words_from_file()

    def get_random_word(self):
        random_number = random.randrange(len(self.words))
        random_word = self.words[random_number]

        return random_word

    def get_random_leveled_word(self):
        your_level = TheLevel()
        leveled_word_list = self.get_leveled_word_list(your_level.get_selected_level_limits())
        random_number = random.randrange(len(leveled_word_list))
        random_word = leveled_word_list[random_number]

        return random_word


    def get_leveled_word_list(self, level_limits):
        leveled_word_list = []
        for word in self.words:
            if len(word) >= level_limits[0] and len(word) <= level_limits[1]:
                leveled_word_list.append(word)

        return leveled_word_list

    def read_words_from_file(self, filename="gpl.txt"):
        file_handle = open(filename, "r")
        file_content = file_handle.read()
        file_handle.close()
        file_content = self.sanitize_string(file_content)
        words_from_file = file_content.split()

        self.words = words_from_file

    def sanitize_string(self, words_string: str):
        fixed_string = words_string.lower()
        fixed_string = re.sub('[^a-z]+', ' ', fixed_string)
        return fixed_string
