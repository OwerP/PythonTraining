"""
Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).

BMI=masa/(wzrost**2)
masa [kg]
wzrost[m]
poniżej 16,0 – wygłodzenie
16,0–17,0 – wychudzenie (spowodowane często przez ciężką chorobę)
17–18,5 – niedowagę
18,5–25,0 – wartość prawidłową
25,0–30,0 – nadwagę
30,0–35,0 – I stopień otyłości
35,0–40,0 – II stopień otyłości
powyżej 40,0 – III stopień otyłości (otyłość skrajna)
"""


wzrost, masa = input('podaj odzielajac przecinkiem wzrost [cm] i masę ciała[kg]: ').split(',')
bmi=100*100*float(masa)/float(wzrost)**2
print (f"Twój BMI to  {bmi} ",end='')
if bmi < 16.0:
    print(f"jesteś wygłodzony")
elif 16.0 <= bmi <= 17.0:
    print(f"jesteś wychudzony")
elif 17.0 < bmi <= 18.5:
    print(f"masz niedowagę")
elif 18.5 < bmi <= 25.0:
    print(f"Masz prawidłowe BMI")
elif 25.0 < bmi <= 30.0:
    print(f"masz nadwagę")
elif 30.0 < bmi <= 35.0:
    print(f"masz I stopień otyłości")
elif 35.0 < bmi <= 40.0:
    print(f"masz II stopień otyłości")
elif 40.0 < bmi:
    print(f"masz III stopień otyłości ")