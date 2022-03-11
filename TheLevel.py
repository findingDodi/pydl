class TheLevel:

    def __init__(self):
        self.level = self.get_level_from_user()
        self.level_easy = (2, 4)
        self.level_medium = (5, 7)
        self.level_hard = (8, 10)
        self.level_extra_hard = (11, 999)
        self.level_random = (2, 999)
        self.level_wordle = (5, 5)

    def get_level_from_user(self):
        print("Choose your level:")
        print("1 = easy (2-4 letters)")
        print("2 = medium (5-7 letters)")
        print("3 = hard (8-10 letters)")
        print("4 = extra hard (11+ letters)")
        print("5 = wordle (5 letters)")
        print("6 = random (2+ letters)")
        user_level = int(input("Enter Level: "))

        return user_level

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

