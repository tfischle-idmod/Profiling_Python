
@profile
def my_func1():
    a = [1] * (10 ** 7)         # 72byte x 10^7 = 72MB; sys.getsizeof([1]): 72

@profile
def my_func2():
    b = [2] * (2 * 10 ** 7)     # 72byte x 2 x 10^7 = 148MB


if __name__ == '__main__':
    my_func1()
    my_func2()

    for _ in range(1000):
        for _ in range(1000):
            pass
