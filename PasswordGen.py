__author__ = '619635'

import random
import string

def pw_generator(size=8, chars=string.ascii_letters+string.punctuation+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

size=int(input("Please enter the size"))
print(pw_generator(size))