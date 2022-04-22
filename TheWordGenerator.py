from TheLevel import TheLevel
import random
import re
import os


class TheWordGenerator:

    def __init__(self):
        self.words = []
        self.read_words_from_file(self.get_wordlist_from_user())

    def get_random_word(self):
        random_number = random.randrange(len(self.words))
        random_word = self.words[random_number]

        return random_word

    def get_random_leveled_word(self):
        word_lengths_from_list = self.get_word_lengths(self.words)
        your_level = TheLevel(word_lengths_from_list)
        leveled_word_list = self.get_leveled_word_list(your_level.get_selected_level_limits())
        #print("******", your_level.get_selected_level_limits())
        random_number = random.randrange(len(leveled_word_list))
        random_word = leveled_word_list[random_number]

        return random_word

    def get_leveled_word_list(self, level_limits):
        leveled_word_list = []
        for word in self.words:
            if len(word) >= level_limits[0] and len(word) <= level_limits[1]:
                leveled_word_list.append(word)

        return leveled_word_list

    def get_wordlist_from_user(self):
        print("Please choose your wordlist:")
        word_lists = os.listdir(path='wordlists')
        counter = 0
        for word_list in word_lists:
            counter += 1
            print(counter, "=", word_list)

        user_word_list_index = int(input("Which wordlist do you want to use? (Enter number): "))

        return word_lists[(user_word_list_index - 1)]

    def get_word_lengths(self, words_array):
        word_set = set()
        for word in words_array:
            word_set.add(len(word))

        return word_set


    def read_words_from_file(self, filename="words.csv"):
        file_handle = open("wordlists/" + filename, "r")
        file_content = file_handle.read()
        file_handle.close()
        file_content = self.sanitize_string(file_content)
        words_from_file = file_content.split()

        self.words = words_from_file

    def sanitize_string(self, words_string: str):
        fixed_string = words_string.lower()
        fixed_string = re.sub('[^a-z]+', ' ', fixed_string)

        return fixed_string
