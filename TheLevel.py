class TheLevel:

    def __init__(self, available_word_lengths):
        self.level_easy = (2, 4)
        self.level_medium = (5, 7)
        self.level_hard = (8, 10)
        self.level_extra_hard = (11, 999)
        self.level_wordle = (5, 5)
        self.level_random = (2, 999)

        self.levels = [
            self.level_easy, self.level_medium, self.level_hard,
            self.level_extra_hard, self.level_wordle, self.level_random
        ]
        self.available_word_lengths = available_word_lengths
        self.available_levels = self.get_available_levels(self.available_word_lengths)
        self.level = self.get_level_from_user()


    def get_level_from_user(self):
        print(self.available_levels)
        print("Choose your level:")
        for level in self.levels:
            for i in self.available_levels:
                if i == level:
                    level_number = (self.levels.index(level) + 1)
                    level_string = ""
                    if level_number == 1:
                        level_string = "easy"
                    if level_number == 2:
                        level_string = "medium"
                    if level_number == 3:
                        level_string = "hard"
                    if level_number == 4:
                        level_string = "extra hard"
                    if level_number == 5:
                        level_string = "wordle"
                    if level_number == 6:
                        level_string = "random"
                    print(level_number, "=", level_string, "(", level[0], "-", level[1], "letters )")

        user_level = int(input("Enter Level: "))

        return user_level

    def get_available_levels(self, available_word_lengths):
        available_levels = set()
        for level in self.levels:
            level_range = list(range(level[0], level[1] + 1))
            for i in available_word_lengths:
                if i in level_range:
                    available_levels.add(level)

        return available_levels

    def get_selected_level_limits(self):
        if self.level == 1:
            return self.level_easy
        if self.level == 2:
            return self.level_medium
        if self.level == 3:
            return self.level_hard
        if self.level == 4:
            return self.level_extra_hard
        if self.level == 5:
            return self.level_wordle
        if self.level == 6:
            return self.level_random

