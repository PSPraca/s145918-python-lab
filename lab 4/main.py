import sys
import this
import random

# zadanie 1

l = list(range(0,51,5))


# zadanie 2

l = int(input("Podaj wysokość: 3, 5, 7 lub 9\n"))
if l not in [3, 5, 7, 9]:
    print("Błędna wysokość")
for i in range(1, l * 2, 2):
    print(("o"*i).center(l) if i < l else ("o"*(l - (i - l))).center(l))


# zadanie 3

s = ""
for i in range(11):
    for j in range(11):
        s += str((i * j) if i * j > 0 else (i + j)).rjust(5)
    s += "\n"

print(s)


# zadanie 4

while True:
    n = input("Podaj liczbę całkowitą. Podaj 'q', aby wyjść.\n")
    if n == "q":
        break
    print(f"Bin: {int(n):b}")
    print(f"Oct: {int(n):o}")
    print(f"Hex: {int(n):x}")


# zadanie 5

while True:
    n = input("Podaj wartość. Podaj 'q' aby wyjść.\n")
    if n == "q":
        break
    try:
        int(n)
    except:
        print("Podana wartość nie jest rzutowalna na int.")
    else:
        print("Podana wartość jest rzutowalna na int.")
    
    try:
        float(n)
    except:
        print("Podana wartość nie jest rzutowalna na float.")
    else:
        print("Podana wartość jest rzutowalna na float.")


# zadanie 6

while True:
    sys.stdout.write("Podaj liczbę. Podaj 'q', aby wyjść\n")
    n = sys.stdin.readline()
    if "q" in n:
        break
    digits = len(n) - 1
    n = int(n)
    s = ""
    while digits > 0:
        s += f"{n // 10 ** (digits - 1)} * 1{'0' * (digits - 1)} + "
        try:
            n = int(str(n)[1:])
        except ValueError:
            break
        digits -= 1
    sys.stdout.write(f"Podaną liczbę można zapisać jako {s[:-3]}\n")


# zadanie 7

s = input("Podaj zdanie do zakodowania.\n")

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))


# zadanie 8

s = sorted(input("Podaj zdanie do zakodowania.\n").split(" "))

print(s)


# zadanie 9

l = [["Koleżanki i koledzy ", "realizacja nakreślonych zadań programowych ", "zmusza nas do przeanalizowania ", "istniejących warunków administracyjno--finansowych."],
["Z drugiej strony ", "zakres i miejsce szkolenia kadr ", "spełnia istotną rolę w kształtowaniu ", "dalszych kierunków rozwoju."],
["Podobnie ", "stały wzrost ilości i zakres naszej aktywności ", "wymaga sprecyzowania i określenia ", "systemu powszechnego uczestnictwa."],
["Nie zapominajmy jednak, że ", "aktualna struktura organizacji ", "pomaga w przygotowaniu i realizacji ", "postaw uczestników wobec zadań stawianych przez organizację."],
["W ten oto sposób ", "nowy model działalności organizacyjnej ", "zabezpiecza udział szerokiej grupie w kształtowaniu ", "nowych propozycji."],
["Praktyka dnia codziennego dowodzi, że ", "dalszy rozwój różnych form działalności ", "spełnia ważne zadania w wypracowaniu ", "kierunków postępowego wychowania."],
["Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ", "stałe zabezpieczenie informacyjno programowe naszej działalności ", "umożliwia w większym stopniu tworzenie ", "systemu szkolenia kadry odpowiadającego potrzebom."],
["Różnorakie i bogate doświadczenia ", "wzmacnianie i rozwijanie struktur ", "powoduje docenianie wagi ", "odpowiednich warunków aktywizacji."],
["Troska organizacji, a szczególnie ", "konsultacja z szerokim aktywem ", "przedstawia interesującą próbę sprawdzenia ", "modelu rozwoju."],
["Wyższe założenia ideowe, a także ", "rozpoczęcie powszechnej akcji kształtowania postaw ", "pociąga za sobą proces wdrażania i unowocześniania ", "form oddziaływania."]]

n = int(input("Podaj ilość zdań do wygenerowania.\n"))

for i in range(n):
    print(f"{l[random.randrange(10)][0]}{l[random.randrange(10)][1]}{l[random.randrange(10)][2]}{l[random.randrange(10)][3]}")