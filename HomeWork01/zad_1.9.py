"""
Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.
"""

for i in range(1,101):
    flag = False
    print (f"{i}",end='')
    if i % 5 == 0:
        print(" Fizz",end='')
        flag=True
    if i % 3 == 0:
        if not flag:
            print(" ",end='')
        print("Buzz",end='')
    print()


