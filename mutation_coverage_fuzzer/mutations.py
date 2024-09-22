from random import randint, choice
from string import ascii_letters


def flip_random_character(initial: str) -> str:
    if not initial:
        return ""
    random_pos = randint(0, len(initial) - 1)
    return (
        initial[:random_pos]
        + chr(ord(initial[random_pos]) << 1)
        + initial[random_pos + 1 :]
    )


def delete_random_character(initial: str) -> str:
    if not initial:
        return ""
    random_pos = randint(0, len(initial) - 1)
    return initial[:random_pos] + initial[random_pos + 1 :]


def insert_random_character(initial: str) -> str:
    if not initial:
        return ""
    random_pos = randint(0, len(initial) - 1)
    return initial[:random_pos] + choice(ascii_letters) + initial[random_pos + 1 :]
