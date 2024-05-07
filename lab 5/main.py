import math

from random import randint

# zadanie 1
A = [1 / x for x in range(1, 10)]
B = [2 ** x for x in range(10)]
C = [x for x in B if x % 4 == 0]


# zadanie 2
matrix = [[randint(0, 10) for x in range(4)] for y in range(4)]
print(list(matrix[x]) for x in range(4))
print([matrix[x][x] for x in range(4)])

# zadanie 3
s = "Ala ma kota"
print([(word, [ord(l) for l in word]) for word in s.split(" ")])

# zadanie 4
def row_kwadratowe(a: float, b: float, c: float) -> tuple[float, float] | float | int:
    delta = d**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(detla)) / (2 * a)
        return x1, x2

# zadanie 5
# mam nadzieję, że nie muszę zakładać, że użytkownik może podać nie-liczbę? :'D
def rzuty() -> tuple[str, str]:
    n = int(input("Podaj liczbę całkowitą:\n"))
    throws = [randint(1, 6) for i in range(n)]
    return [(f"oczka: {x}", f"rzuty: {throws.count(x)}") for x in set(throws)]

print(rzuty())

# zadanie 6
def ciag(*s: str) -> str:
    if len(s) < 1:
        return ''
    return sorted(s)

print(ciag("ghf", "sfgsdfg", "fasdsf", "fawead", "awedfs"))

# zadanie 7
def weird_sum(**kwargs) -> int:
    result = 0 
    for key in kwargs.keys():
        result += kwargs[key]
    return result

print(weird_sum(f=243, p=3425, g=123))
