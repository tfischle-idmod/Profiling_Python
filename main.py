
def computation():
    a = range(int(1e6))
    b = range(int(1e6))
    result = 0
    for x, y in zip(a, b):
        result += x + y
    return result


def function1():
    for _ in range(10):
        computation()


def function2():
    for _ in range(5):
        computation()


def main_fct():
    for _ in range(10000):
        for _ in range(1000):
            pass
    function1()
    function2()
    function1()


if __name__ == '__main__':
    main_fct()
