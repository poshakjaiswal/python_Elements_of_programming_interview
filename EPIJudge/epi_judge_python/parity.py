from test_framework import generic_test

"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
"""


def parity(x: int) -> int:
    # TODO - you fill in here.
    total_set_bits = 0
    while x:
        total_set_bits += (x & 1)
        x = x >> 1

    return total_set_bits % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
