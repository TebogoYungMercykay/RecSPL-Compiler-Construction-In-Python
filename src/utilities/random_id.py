import string
import random


def generate_random_id(length=20):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))
