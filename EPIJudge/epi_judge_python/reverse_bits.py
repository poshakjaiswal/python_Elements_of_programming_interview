from test_framework import generic_test

PRECOMPUTED_REVERSE = {}


def swap_bits(x, i, j):
    # firstly check if the bits are just the same
    if (x >> i & 1) != (x >> j & 1):
        bit_mask = 1 << i | 1 << j
        # create a new bit mask
        x = x ^ bit_mask  # since we will be masking with 000001100 , xor with 0 bit doesn't change the output

    # TODO - you fill in here.
    return x


def reverse_bits1(x: int) -> int:
    # TODO - you fill in here.
    # reverse_bits_brute_force_by_swapping
    # keep swapping the bits
    total_bit_length = x.bit_length()

    msb_position = total_bit_length
    lsb_position = 0

    while msb_position != lsb_position:
        swap_bits(x, msb_position, lsb_position)

    return x


def reverse_bits(x: int) -> int:  # reverse bit using hashing
    mask_size = 2  # trying with 8 bit sample , by shifting just two bits
    bit_mask = 96

    # input-> 10010011 , 147
    # output should be -> 11001001 , 201
    PRECOMPUTED_REVERSE[0] = 0  # 0,0 -> 0,0
    PRECOMPUTED_REVERSE[1] = 2  # 0,1 -> 1,0
    PRECOMPUTED_REVERSE[2] = 1  # 1,0 -> 0,1
    PRECOMPUTED_REVERSE[3] = 3  # 1,1-> 1,1

    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size)
            | PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size)
            | PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size
            | PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask])


if __name__ == '__main__':
    print(reverse_bits(147))
    # exit(
    #     generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
    #                                    reverse_bits))
