'''population = int(373582814)
for i in range(5):
    population += 5256000 - 2102400 + 700800
    print(population)
'''

minute = int(input())
days = minute//1440
year = days//365
days = days%365

print(minute,"minutes is approximately",year,"year(s) and",days,"day(s)")
