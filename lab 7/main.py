from typing import Any

# zadanie 1
def extract_numbers(vals: list[Any]) -> list[int | float]:
    f = filter(lambda x : isinstance(x, int) or isinstance(x, float), vals)
    return [x for x in f]
print(extract_numbers(['f', 15, 1.5, 'dsawd', '15', 23, 0]))

# zadanie 2
s = input('Podaj kilka wyrazów:\n').split()
print(sorted(s, key=lambda x : len(x)))

# zadanie 3
def weird_sort(l: list[int | str], reversed: bool = True) -> list[int | str]:
    if reversed:
        return [sorted(filter(lambda x : isinstance(x, int), l)), sorted(filter(lambda x : isinstance(x, str), l))]
    else:
        return [sorted(filter(lambda x : isinstance(x, str), l)), sorted(filter(lambda x : isinstance(x, int), l))]
print(weird_sort(['a', 'b', 1, 2]))

# zadanie 4
def do_stuff(poland: bool = True) -> None:
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
    if poland: 
        with open('zamowienia_polska.csv', 'w') as f:
             f_writer = csv.writer(f)
             for row in pl:
                 f_writer.writerow(row)

    else:
        with open('zamowienia_niemcy.csv', 'w') as f:
            f_writer = csv.writer(f)
            for row in de:
                f_writer.writerow(row)

# zadanie 5
def dict_sort(d: dict, method: callable) -> dict:
    print([sum(x[1]) for x in d.items()])
    return sorted(d.items(), key=lambda x : method(x[1]))

print(dict_sort({'Jan': [1, 2, 3, 5], "Paweł": [0, 20], "aaaaaaaaaaaaaaaaa": [1]}, sum))
