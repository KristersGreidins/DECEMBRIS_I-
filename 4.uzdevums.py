"""Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
Izmantojiet GIT, lai izsekotu kodu un veidotu komitus."""

ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

if ievaditais_skaitlis<0:
    print("Faktoriāls neatbilst negatīviem skaitļiem")
else:
    faktorials=1

for skaitlis in range(ievaditais_skaitlis +1):

    print(f'{ievaditais_skaitlis}! = {faktorials}')