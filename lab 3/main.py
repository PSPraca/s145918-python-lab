import string

# zad 1
l = []
for i in range(1, 10):
    l.append(i)

l1 = l[len(l)//2:]
print(f"Oryginał: {l}")
l = l[:len(l)//2]
print(f"l1: {l1}")
print(f"Zmienione l: {l}")

# zad 2
l_join = [0] + l + l1
l_copy = l_join
print(f"Połączone: {l_join}")
print(f"Kopia: {l_copy}")
l_copy.sort(reverse=True)
print(f"Posortowane: {l_copy}")

# zad 3
s = input("Wprowadź ciąg znaków\n").lower()
s_set = set(s)
sorted(s_set, reverse=True)
print(s_set)

# zad 4
months_pl = {}
months_names_pl = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
for i in range(1, 13):
    months_pl[i] = months_names_pl[i - 1]
print(months_pl)

# zad 5
months_eng = {}
months_names_eng = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
for i in range(1,13):
    months_eng[i] = months_names_eng[i - 1]
months = {"pl": months_pl, "eng": months_eng}
print(months)

# zad 6
s = "Marianna"
print(dict.fromkeys(set(s), 1)) # tak, można tu podać set jako drugą wartość i wtedy będzie ona dynamicznie przypisana

# zad 7
s = input("Wprowadź ciąg znaków\n")
print(f"Wprowadzony ciąg znaków: {s}")
print(f"Długość: {len(s)}")
print(f"Pokrywających się ze string.ascii_lowercase: {len(set(s).intersection(set(string.ascii_lowercase)))}")
print(f"Pokrywających się ze string.digits: {len(set(s).intersection(set(string.digits)))}")