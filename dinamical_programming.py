# Рекурентный алгоритм вычисления чисел Фибоначчи (так нельзя писать - очень медленно)
def fib(n):
    """
    Slowly Fibonacci
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Работает быстро
def fib2(n):
    """
    Fast Fibonacci
    :param n:
    :return:
    """
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Количество траекторий движения кузнечика
def trage_num(n):
    """
    Traekitories amount
    :param n:
    :return:
    """
    K = [0, 1] + [0]*n
    for i in range(2, n+1):
        K[i] = K[i-2] + K[i-1]
    return K[n]

if __name__ == '__main__':
    print(fib(14))
    print(fib2(100))
    print(trage_num(99))