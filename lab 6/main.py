import csv

from datetime import datetime
from random import randint
from itertools import permutations

# zadanie 1
# pl = []
# de = []
# with open("zamowienia.csv", "r") as f:
#     f_reader = csv.reader(f, delimiter=';')
#     for row in f_reader:
#         if 'Kraj' in row:
#             continue
#         row[-1] = row[-1][:-4]
#         row[-1].replace(',', '.')
#         row[-1].replace(' ', '')
#         row[2] = datetime.strftime(datetime.strptime(row[2], "%d.%m.%Y"), "%Y-%m-%d")
#         if row[0] == "Polska":
#             pl.append(row)
#         else:
#             de.append(row)

# with open('zamowienia_polska.csv', 'w') as f:
#     f_writer = csv.writer(f)
#     for row in pl:
#         f_writer.writerow(row)

# with open('zamowienia_niemcy.csv', 'w') as f:
#     f_writer = csv.writer(f)
#     for row in de:
#         f_writer.writerow(row)

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
    colors = ['kier', 'karo', 'trefl', 'pik']
    stack = []
    for color in colors:
        stack += [x + ' ' + color for x in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']]
    players = ['p1', 'p2', 'p3', 'p4']
    hands = {}
    for p in players:
        hands |= {p: []}
        for i in range(5):            
            added_card = stack[randint(0, len(stack) - 1)]
            hands[p] += [added_card]
            stack.remove(added_card)
        print(hands[p])

# cards()

# zadanie 8
def emails(domain: str) -> None:
    with open('names.txt', 'r') as f:
        names = f.readlines()
    for name in names:
        name = name.replace('\n', '')
        mail = name.lower().replace('ą', 'a').replace('c', 'ć').replace('ń', 'n').replace('ł', 'l').replace('ś', 's').replace('ę', 'e').replace('ó', 'o').replace(' ', '.') + '@' + domain
        print(f"{name}, {mail}")

# emails('gmail.com')

# zadanie 9
with open('hasla.txt', 'r') as f:
    words = f.readlines()

words = [x.replace('\n', '') for x in words]
chosen_word = words[randint(0, len(words) - 1)]

print('haslo:')
print(''.join(['_' if x != ' ' else x for x in chosen_word]))

revealed_letters = [' ']

while True:
    c = input('Podaj literę bądź całę hasło:\n')
    if len(c) > 1:
        if chosen_word.lower() == c.lower():
            print("gratulacje, wygrałeś")
            break
        else:
            print('niestety to nie jest hasło')
    if c.lower() not in chosen_word.lower():
        print('w haśle nie występuje ta litera')
    elif c.lower() not in revealed_letters:
        revealed_letters.append(c.lower())
    else:
        print("podawałeś już tą literę")
    if len(revealed_letters) == len(set(chosen_word.replace(' ', ''))):
        break
    print(''.join(['_' if x.lower() not in revealed_letters else x for x in chosen_word]))
