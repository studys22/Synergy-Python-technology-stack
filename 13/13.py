import random
import math

n, m, max_num = map(int, input("N, M, Maximum number: ").split())


def rand_list():
    a = [[random.randint(0, max_num) for j in range(m)] for i in range(n)]
    return a


def sum_matr(a, b):
    c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
    return c


def print_matr(a, name, width):
    print(f"\n\n{name}:")
    formatstring = f"{{:{width + 1}d}}"
    for i in range(n):
        for j in range(m):
            print(formatstring.format(a[i][j]), end="")
        print()


random.seed()
a = rand_list()
b = rand_list()
c = sum_matr(a, b)
digits_in_max_num = math.ceil(math.log10(max_num + 1))
digits_in_max_num2 = math.ceil(math.log10(2*max_num + 1))
print_matr(a, "A", digits_in_max_num)
print_matr(b, "B", digits_in_max_num)
print_matr(c, "A + B", digits_in_max_num2)
