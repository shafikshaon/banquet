from datetime import datetime

__author__ = 'Shafikur Rahman'


def generate_random_number():
    generated_number = int(datetime.now().timestamp() * 1000)
    return generated_number
