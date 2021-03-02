from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    result, powers = 1.0, y
    """
    The only change when y is negative is replacing x by 1/x and y by -y. ln the implementation below we replace the recursion with a while loop to avoid the overhead of function calls.
    """
    if y < 0:
        x = 1.0 / x
        powers = -powers  # converting negative to positive
    iteration = 0  # only as a debugging variable
    while powers:
        # if the least significant bit of y is 0, the result is  ((x)^(y/2))^2  otherwise, it is x*((x)^(y/2))^2
        if powers & 1:
            print("inside")
            result = result * x
        x = x * x
        powers = powers >> 1
        iteration += 1
    return result


if __name__ == '__main__':
    print(power(2.0, 7))
    # exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv', power))
