# Проверка эквивалентности строк
def equal(A, B):
    """
    Check equal of strings
    :param A:
    :param B:
    :return:
    """
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True
if __name__ == "__main__":
    print(equal('эрмитаж', 'эрмитаж'))