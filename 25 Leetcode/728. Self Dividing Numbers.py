def selfDividingNumbers(left, right):

    def is_self_dividing(num):
        if '0' not in str(num):
            return False
        for digit in str(num):
            if  num % int(digit) != 0:
                return False

        return True

    x = filter(is_self_dividing, range(left, right + 1))
    print(x)
    return x

print(selfDividingNumbers(10,23))