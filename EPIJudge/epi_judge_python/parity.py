from test_framework import generic_test

"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
"""

PRECOMPUTED_PARITY = {}


# 2 bit caches as an example for pre computation
def fill_precomputed_parity(x: int) -> int:
    # x expected to be a 8 bit number
    # x = 234  # 11101010
    PRECOMPUTED_PARITY[0] = 0
    PRECOMPUTED_PARITY[1] = 1
    PRECOMPUTED_PARITY[2] = 1
    PRECOMPUTED_PARITY[3] = 0
    bit_mask = 3
    mask_size = 2

    return PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^ PRECOMPUTED_PARITY[
        ((x >> (2 * mask_size)) & bit_mask)] ^ PRECOMPUTED_PARITY[
               ((x >> (1 * mask_size)) & bit_mask)] ^ PRECOMPUTED_PARITY[(x & bit_mask)]
    # 11101010  ==> 


def parity(x: int) -> int:
    x = x ^ 64
    x = x ^ 32
    x = x ^ 16
    x = x ^ 8
    x = x ^ 4
    x = x ^ 2
    x = x ^ 1
    return x & 0x1


def parity2(x: int) -> int:
    # parity_by_dropping_lower_bits

    total_set_bits = 0
    while x:
        """
              Performing xor means 0,0 -> 0 , 0,1->1 , 1,1-> 0 , we are only tracing the odd one out , no need to do mod operator in the end 
               """
        total_set_bits = total_set_bits ^ 1  # xor operator
        """
        The first improvement is based on erasing the lowest set bit in a word in a single operation,
thereby improving performance in the best- and average-cases
        """
        x = x & (x - 1)

    return total_set_bits


def parity1(x: int) -> int:
    # TODO - you fill in here.
    total_set_bits = 0
    while x:
        total_set_bits += (x & 1)
        x = x >> 1

    return total_set_bits % 2


if __name__ == '__main__':
    # print(fill_precomputed_parity(3))
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
