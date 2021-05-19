"""
Napisz program, który na podstawie wprowadzonych wymiarów opakowania (x, y, z) obliczy jego objętość oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).
"""

x, y, z = input('podaj wymiary opakowania [cm] ').split(',')
v = float(x) * float(y) * float(z)
print(f"objętość opakowania  {v} cm^3 ", end='')
if v > 1000:
    print(f"jest ona powyżej 1 litra")
else:
    print(f"jest ona poniżej 1 litra")
