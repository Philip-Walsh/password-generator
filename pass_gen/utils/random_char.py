"""Random Character utilizes the random package to retrun chars of type"""
from random import randint, choice


class RandomChar:
    """Random Character Class"""
    def __init__(self):
        self._uppercase_range = (65, 90)
        self._number_range = (48, 57)
        # self._special_range = (33, 152)
        # self._lowercase_range = (97, 122)

    def _get_random(self, tuple_range):
        "Gets a random integer from a range of numbers and returns a character"
        return chr(randint(*tuple_range))

    def upper_char(self):
        "Gets random upper case character"
        return self._get_random(self._uppercase_range)

    def lower_char(self):
        "Gets random lower case character"
        return self.upper_char().lower()

    def number_char(self):
        "Gets random number character"
        return self._get_random(self._number_range)

    def special_char(self):
        "Gets random special character"
        return choice(list("~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"))
