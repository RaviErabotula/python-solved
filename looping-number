#Q: https://datalemur.com/questions/python-looping-number


def is_looping(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n != 1
