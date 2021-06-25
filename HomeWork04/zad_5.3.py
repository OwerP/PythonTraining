'''
Podstawowa funkcjonalność:
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie słowa występujące w pliku wraz z informacją ile razy dane słowo występuje. Na przykład w ten sposób:

```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```

Ewentualne uproszczenie (w razie problemów z wypisywaniem): wypisz tylko jedno najczęściej występujące słowo.

Dalsze rozszerzenia (opcjonalnie):
- posortuj wypisywane słowa
- oprócz liczby poszczególnych słów policz i wypisz także liczbę wszystkich słów, łączną liczbę wszystkich znaków.
'''


from collections import defaultdict
import re
import icu
regex = r"([^\s!,.—:;\)\(?]*)"

collator = icu.Collator.createInstance(icu.Locale('pl_PL.UTF-8'))

try:
    file_name = 'pan-tadeusz.txt'

    words=defaultdict(int)
    with open(file_name,encoding='utf8') as file:
        for line in file:
            line=line.lower()
            list_of_words=re.findall(r'([^ «»,!,.—:;…\)\(?*/\n]+)', line)
            for word in list_of_words:
                words[word] +=1
            #matches=re.finditer(r'([^ !,.—:;\)\(?]*)', line)
            xxx='xxx'
        words_total_count = 0
        char_total_count = 0


        for word in sorted(list(words),key=collator.getSortKey):
            words_total_count += int(words[word])
            char_total_count  += len(word)*int(words[word])
            print(f'{word} -> {words[word]}')

        print(f'\nCałkowita liczba słów {words_total_count}, całkowita liczba znaków w tych słowach {char_total_count}')


except FileNotFoundError:
    print(f'File {file_name} not found.')
    exit(1)
except IndexError:
    print(f'File name not provided.')
    exit(1)