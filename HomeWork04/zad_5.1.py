'''
Plik CSV z danymi: https://students.alx.pl/~pgradzinski/kpython/zawodnicy.csv

Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:

1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:

```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```

4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników.
'''

#stat=[MinWeight,MaxWeight,MinHeight,MaxHeight]
from collections import defaultdict

player_extremum ={
'MinWeight': [None,None],
'MaxWeight': [None,None],
'MinHeight': [None,None],
'MaxHeight': [None,None],
}


try:
    file_name = 'zawodnicy.csv'

    country_players_stats=defaultdict(lambda:[0,0,0,0])
    with open(file_name,encoding='utf8') as file:
        for line in file:
            f_name, l_name, country, year, h, w = line.split(';')
            height=int(h)
            weight=int(w)
            country_players_stats[country][0] += 1      # counter
            country_players_stats[country][1] += height #sum of heigh
            country_players_stats[country][2] += weight #sum of weight
            country_players_stats[country][3] = round(country_players_stats[country][1]/country_players_stats[country][0],2)  #avg
            if (player_extremum['MinWeight'][1] is None or player_extremum['MinWeight'][1] > weight):
                player_extremum['MinWeight'][0]=f_name+' '+l_name
                player_extremum['MinWeight'][1]=weight
            if (player_extremum['MaxWeight'][1] is None or player_extremum['MaxWeight'][1] < weight):
                player_extremum['MaxWeight'][0]=f_name+' '+l_name
                player_extremum['MaxWeight'][1]=weight
            if (player_extremum['MinHeight'][1] is None or player_extremum['MinHeight'][1] > height):
                player_extremum['MinHeight'][0] = f_name + ' ' + l_name
                player_extremum['MinHeight'][1] = height
            if (player_extremum['MaxHeight'][1] is None or player_extremum['MaxHeight'][1] < height):
                player_extremum['MaxHeight'][0] = f_name + ' ' + l_name
                player_extremum['MaxHeight'][1] = height

    print (f"W śród skoczków: \n"
       f"\tNajwyższy to {player_extremum['MaxHeight'][0]} {player_extremum['MaxHeight'][1]} cm\n "
       f"\tNajniższy to {player_extremum['MinHeight'][0]} {player_extremum['MinHeight'][1]} cm\n"
       f"\tNajcięższy to {player_extremum['MaxWeight'][0]} {player_extremum['MaxWeight'][1]} kg\n"
       f"\tNajlżejszy to {player_extremum['MinWeight'][0]} {player_extremum['MinWeight'][1]} kg\n")

    print("Statystyki krajów wg notacji: \nCountry - NoOfPlayers:SumOfWeight:AvgHeight")
    for country, list_of_stat in country_players_stats.items():
        print (f'{country} - {list_of_stat[0]}:{list_of_stat[2]}:{list_of_stat[3]}')

except FileNotFoundError:
    print(f'File {file_name} not found.')
    exit(1)
except IndexError:
    print(f'File name not provided.')
    exit(1)