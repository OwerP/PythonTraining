"""
Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za pięć kilo ziemniaków.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
"""

cena_1kg_ziemniakow = float(input('ile kosztuje kilo ziemniaków [PLN]: '))
print(f" w takim razie za 5 kg zapłacisz {round(5*cena_1kg_ziemniakow,2)} PLN")

cena_1kg_ziemniakow, ilosc_kg = input('podaj odzielajac przecinkiem cenę za kg ziemniaków [PLN] i ile chcesz kupić[kg]: ').split(',')
print(f" w takim razie za 5 kg zapłacisz {round(float(ilosc_kg)*float(cena_1kg_ziemniakow),2)} PLN")

cena_1kg_ziemniakow, ilosc_kg_z = input('podaj odzielajac przecinkiem cenę za kg ziemniaków [PLN] i ile chcesz kupić[kg]: ').split(',')
cena_1kg_bananow, ilosc_kg_b = input('podaj odzielajac przecinkiem cenę za kg bananów [PLN] i ile chcesz kupić[kg]: ').split(',')

koszt_ziemniakow=float(ilosc_kg_z)*float(cena_1kg_ziemniakow)
koszt_bananow=float(ilosc_kg_b)*float(cena_1kg_bananow)

if koszt_ziemniakow > koszt_bananow:
    print (f"za ziemniaki trzeba zaplacić więcej o {round(koszt_ziemniakow - koszt_bananow,2)} PLN")
elif koszt_ziemniakow < koszt_bananow:
    print(f"za ziemniaki trzeba zaplacić więcej 0 {round(koszt_bananow - koszt_ziemniakow,2) } PLN")
else:
    print(f"banany i ziemniaki będą w tym samym koszcie {koszt_bananow} PLN ")



