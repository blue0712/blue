def getDigit(x):
    """

    :type x : int or float
    """
    returnDigit = 0
    while x > 0:
        returnDigit += 1
        x //= 10
    return returnDigit


print(getDigit('1024'))
print(getDigit(2 ** 32))
