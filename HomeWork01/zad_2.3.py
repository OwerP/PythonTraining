"""
Napisz program, który odczytuje od użytkownika wiele liczb.

Program powinien wyliczyć i na końcu wypisać następujące statystyki:

- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum

NIE używaj funkcji wbudowanych!
"""
var_min = None
var_max = None
var_sum = None
var_avg = None
var_counter = 0
var_tmp_str = None
var_tmp_digit = None

while True:
    var_tmp_str = input('Podaj liczbę lub q: ')
    if var_tmp_str.lower() == 'q':
        break

    try:
        var_tmp_digit = float(var_tmp_str)
    except ValueError:
        print('Podałeś nieprawidłową liczbę.')
        continue
    var_counter +=1
    if var_sum is None :
        var_sum=var_tmp_digit
    else:
        var_sum +=var_tmp_digit
    if var_counter !=0:
        var_avg = var_sum/var_counter

    if var_min is None or var_tmp_digit < var_min:
        var_min = var_tmp_digit

    if var_max is None or var_tmp_digit > var_max:
        var_max = var_tmp_digit


if var_min is None:
    print('Nie wprowadziles zadnej liczby')
else:
    print(f'liczba podanych liczb  {var_counter}')
    print(f'suma liczb  {var_sum}')
    print(f'średnia liczb  {var_avg}')
    print(f'minimum liczb  {var_min}')
    print(f'minimum liczb  {var_max}')

