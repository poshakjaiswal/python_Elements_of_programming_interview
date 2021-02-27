from test_framework import generic_test


def swap_bits(x, i, j):
    # firstly check if the bits are just the same
    if (x >> i & 1) != (x >> j & 1):
        bit_mask = 1 << i | 1 << j
        # create a new bit mask
        x = x ^ bit_mask  # since we will be masking with 000001100 , xor with 0 bit doesn't change the output
        
    return x


if __name__ == '__main__':
    # print(swap_bits(8, 0, 3))
    exit(generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv', swap_bits))
