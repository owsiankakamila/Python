wyraz = input("Podaj wyrazenie: ")

wyraz = wyraz.casefold()
print(wyraz)
re_wyraz = reversed((wyraz))

if list(wyraz) == list(re_wyraz):
    print("To palindrom!")
else:
    print("to nie palindrom")
