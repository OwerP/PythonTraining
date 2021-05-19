"""
Napisz program obliczający średnią wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.
"""
import statistics
a = list(map(float,input("podaj temeperatury ze wszystkich pomiarów z tyg oddzielone przecinkiem: ").strip().split(',')))

print (f"średnia podanych temperatur wynosi {statistics.mean(a)}")

