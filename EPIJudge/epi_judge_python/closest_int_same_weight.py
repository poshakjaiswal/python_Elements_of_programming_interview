from test_framework import generic_test


def swap_bits(x, i, j):
    # firstly check if the bits are just the same
    if (x >> i & 1) != (x >> j & 1):
        bit_mask = 1 << i | 1 << j
        # create a new bit mask
        x = x ^ bit_mask  # since we will be masking with 000001100 , xor with 0 bit doesn't change the output

    return x


def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):  # go from 0 to 63 bit
        if (x >> i) & 1 != (x >> (i + 1)) & 1:  # find the right most two consecutive bits which differ and swap them
            # x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i +1) return x
            x = swap_bits(x, i, i + 1)
            return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
