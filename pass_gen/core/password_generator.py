"""Password Generator"""
from random import shuffle, choice
from pass_gen.utils.random_char import RandomChar


DEFAULT_CHAR_TYPE_MIN = 2
DEFAULT_PASSWORD_LENGTH = 12
options = ['upper', 'lower', 'number', 'special']


class PasswordGenerator:
    """Contains methods to Generate a random password"""
    def __init__(self,
                 upper_min=DEFAULT_CHAR_TYPE_MIN,
                 lower_min=DEFAULT_CHAR_TYPE_MIN,
                 number_min=DEFAULT_CHAR_TYPE_MIN,
                 special_min=DEFAULT_CHAR_TYPE_MIN,
                 ):
        self.min_length = DEFAULT_PASSWORD_LENGTH
        self._random = RandomChar()
        self._min = {
            "upper": upper_min,
            "lower": lower_min,
            "number": number_min,
            "special": special_min,
        }

    def get_char(self, char_type):
        """Gets a random character of a given type"""
        char_function = getattr(self._random, f"{char_type}_char")
        return char_function()

    def generate_password(self, length=None):
        """Returns a random password for a given length"""
        if not length:
            length = self.min_length
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
