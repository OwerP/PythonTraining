"""
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
"""

dni_tyg=('pn','wt','sr','cz','pt','so','ne')
dzien_oddania, czas_naprawy = input('podaj odzielajac przecinkiem dzień oddania butów do naprawy  i jej czas np pn,17: ').split(',')
print (f"index {dni_tyg.index(dzien_oddania)}")

dzien_odbioru=(dni_tyg.index(dzien_oddania)+1+int(czas_naprawy)) % 7
print (f"odbiór butów w {dni_tyg[dzien_odbioru -1]} ")

