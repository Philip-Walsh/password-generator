from random import randint, shuffle, choice


class RandomChar:
    def __init__(self):
        """"""
        self._uppercaseRange = (65, 90)
        self._lowercaseRange = (97, 122)
        self._numberRange = (48, 57)
        self._specialRange = (33, 152)

    def _get_random(self, tuple_range):
        return chr(randint(*tuple_range))

    def upper_char(self):
        return self._get_random(self._uppercaseRange)

    def lower_char(self):
        return self._get_random(self._lowercaseRange)

    def number_char(self):
        return self._get_random(self._numberRange)

    def special_char(self):
        # return self._get_random(self._specialRange)
        return choice(list("~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"))


minDefault = 2
options = ['upper', 'lower', 'number', 'special']


class PasswordGenerator:
    def __init__(self,
                 minLength=12,
                 upperMin=minDefault,
                 lowerMin=minDefault,
                 numberMin=minDefault,
                 specialMin=minDefault,
                 ):
        self.minLength = minLength
        self._random = RandomChar()
        self._min = {
            "upper": upperMin,
            "lower": lowerMin,
            "number": numberMin,
            "special": specialMin,
        }

    def get_char(self, char_type):
        char_function = getattr(self._random, f"{char_type}_char")
        return char_function()

    def generate_password(self, length=None):
        if not length:
            length = self.minLength
        password = ""
        for char_type in options:
            for _ in range(self._min[char_type]):
                password += self.get_char(char_type)

        while len(password) < length:
            password += self.get_char(choice(options))

        def _shuffle_password():
            tmp = list(password)
            shuffle(tmp)
            return ''.join(tmp)
        return _shuffle_password()
