"""
Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.
na wejsciu: [49, 50, 20, 40, 35, 10]
na wyjsciu: [49, 10, 20, 40, 35, 50]

Jak to zrobimy?
1. Musimy znaleźć indeks elementu o największej wartosci
i indeks elementu o najmniejszej wartości
2. Zamiana miejscami elementów z tych indeksów

Wersja A
1. używamy pętli for do znalezienia indeksów, patrz zadanie basics/zad_14
2. Zamieniamy wartości pod tymi indeksami

Wersja B
1. Używając funkcji min(), max() znajduje najmniejszą i najwieksza wartosc
2. Znajduję indeks tych elementów w liscie
3. Zamieniam te elementy miejscami
"""
var_in = [49, 50, 20, 40, 35, 10]
#var_out = [49, 10, 20, 40, 35, 50]
#print(f"{var_in.index(min(var_in))} {var_in.index(max(var_in))}")

print(f"tablica przed zmianami {var_in}")
var_in[var_in.index(min(var_in))], var_in[var_in.index(max(var_in))] = var_in[var_in.index(max(var_in))], var_in[var_in.index(min(var_in))]
print(f"tablica po zmianach {var_in}")

