def divide(x, y):
    def add(a, b):
        running_sum1, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum1 |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
        return running_sum1 | carryin

    running_sum = 0

    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x = x >> 1
        y = y << 1

    return running_sum


if __name__ == '__main__':
    first, second = 13, 9
    print(divide(first, second))
