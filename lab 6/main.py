import csv

from datetime import datetime
from random import randint

# zadanie 1
pl = []
de = []
with open("zamowienia.csv", "r") as f:
    f_reader = csv.reader(f, delimiter=';')
    for row in f_reader:
        if 'Kraj' in row:
            continue
        row[-1] = row[-1][:-4]
        row[-1].replace(',', '.')
        row[-1].replace(' ', '')
        row[2] = datetime.strftime(datetime.strptime(row[2], "%d.%m.%Y"), "%Y-%m-%d")
        if row[0] == "Polska":
            pl.append(row)
        else:
            de.append(row)

with open('zamowienia_polska.csv', 'w') as f:
    f_writer = csv.writer(f)
    for row in pl:
        f_writer.writerow(row)

with open('zamowienia_niemcy.csv', 'w') as f:
    f_writer = csv.writer(f)
    for row in de:
        f_writer.writerow(row)

# zadanie 2
def join_files(new_file, *files):
    rows = []
    for file in files:
        with open(file, 'r') as f:
            rows += f.readlines()
    with open(new_file, 'w') as f:
        f.writelines(rows)

# zadanie 3
def f(k: int, l: list[int], max: bool):
    for i in l:
        if type(i) != type(0):
            return 'Podano nie-liczbę'

    l.sort(reverse=max)
    return l[:k]

# print(f(6, [randint(1, 1000) for i in range(100)], not True))

# zadanie 4
def f(l: list):
    result = {}
    for element in l:
        if str(type(element)).split(' ')[-1].replace('>', '').replace("'", '')  not in result.keys():
            result[str(type(element)).split(' ')[-1].replace('>', '').replace("'", '')] = [element]
        else:
            result[str(type(element)).split(' ')[-1].replace('>', '').replace("'", '')] += [element]
    return result

mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
#print(f(mieszana))

# zadanie 5
def f(names: list[str]):
    names.sort()
    with open('A-M_nazwiska.txt', 'w') as f:
        for n in names:
            if ord(n[0]) < ord('N') or n[0] in ['Ą', 'Ć', 'Ę', 'Ł']:
                f.write(n + '\n')
                names.remove(n)
    with open('N-Ż_nazwiska.txt', 'w') as f:
        for n in names:
            if ord(n[0]) < ord('N'):
                continue
            f.write(n + '\n')

# f(['Paweł', 'Łachim', 'Adam'])

# zadanie 6
def reverse_words(s: str):
    result = ""
    for word in s.split():
        result += word[::-1] + ' '
    return result

# print(reverse_words('Ala ma kota'))

# zdanie 7
def cards():
    pass
