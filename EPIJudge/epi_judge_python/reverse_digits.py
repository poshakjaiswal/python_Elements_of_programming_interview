from test_framework import generic_test


def reverse0(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    x_remaining = abs(x)

    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining = x_remaining // 10

    return -result if x < 0 else result


# Bad runtime complexity
def reverse(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    y = x
    x = abs(x)
    number_of_digits = len(str(x)) - 1

    while x:
        lsb = x % 10  # get the last number
        temp = lsb * (10 ** number_of_digits)
        result += temp
        x = x // 10
        number_of_digits = number_of_digits - 1

    return -result if y < 0 else result


if __name__ == '__main__':
    # print(reverse(1245))
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
