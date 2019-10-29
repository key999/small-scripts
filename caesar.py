#!/usr/bin/env python3
from string import ascii_lowercase


def caesar(clear_text, shift):
    output = ""
    for i in range(len(clear_text)):
        if clear_text[i] not in ascii_lowercase:
            output += clear_text[i]
            continue
        output += ascii_lowercase[(ascii_lowercase.find(clear_text[i]) + shift) % len(ascii_lowercase)]

    return output


if __name__ == "__main__":
    try:
        shift = int(input("shift: "))
        shift = -shift if input("code / decode? (C/d): ") == "d" else shift

        print(caesar(input("input: "), shift))
    except ValueError as e:
        print(e)
