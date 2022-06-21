import string
import random


def random_str(char_num):
    return ''.join(random.choice(string.ascii_letters)
                   for _ in range(char_num))
