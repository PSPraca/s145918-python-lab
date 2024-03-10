import random

s = ""

# # zad 1
# if not s:
#     s = input("Wprowadź ciąg znaków rozdzielony separatorem\n")
# sep_in = input("Wprowadź użyty separator\n")
# sep_out = input("Wprowadź nowy separator\n")

# print(f"Oryginał: {s}")
# print(f"Odseparowany: {s.split(sep_in)}")
# print(f"Nowy separator: {str.join(sep_out, s.split(sep_in))}")

# zad 2
# if not s:
#     s = input("Wprowadź ciąg znaków:\n")
# print(f"Oryginał: {s}")
# print(f"Pierwsza połowa: {s[:len(s)//2]}")
# print(f"Druga połowa: {s[len(s)//2:]}")
# print(f"Co drugi znak od tyłu: {s[-2:0:-2]}")

# # zad 3
# if not s:
#     s = input("Wprowadź ciąg znaków\n")

# print(s.title())
# print(s.capitalize())
# print(s.zfill(56))
# print(s.upper())
# print(s.count("a"))
# print(s.center(56))

# # zad 4
# if not s:
#     s = input("Wprowadź ciąg znaków\n")
# print(f"s.isalpha(): {s.isalpha()}")
# print(f"s.isascii(): {s.isascii()}")
# print(f"s.isprintable(): {s.isprintable()}")
# print(f"s.istitle(): {s.istitle()}")
# print(f"s.isupper(): {s.isupper()}")
# print(f"s.isdecimal(): {s.isdecimal()}")

# zad 5 - plik zad_5.py

# zad 6
for i in range(10):
    print(chr(random.randrange(123, 254, 1)))