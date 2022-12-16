import random
import string


def generate_code():
    alphabet = (string.ascii_lowercase
                + string.ascii_uppercase
                + string.digits
                + string.punctuation)
    temp = random.sample(alphabet, 20)
    return ''.join(temp)
