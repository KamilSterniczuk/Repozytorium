import requests
import pandas
from bs4 import BeautifulSoup
temp_d = []
temp_n = []
data = []

result = requests.get("https://www.meteoprog.pl/pl/weather/Gdynya/#1")
src = result.content
soup = BeautifulSoup(src, 'lxml')

def Temperatura():
    i = 0
    tempdata = soup.find_all(attrs={'class': 'dayoffMonth'})
    for tdata in tempdata:
        i += 1
        data.append(tdata.text.split())

    tempdzien = soup.find_all(attrs={'class': 'to'})
    for tempd in tempdzien:
        temp_d.append(tempd.text.split())

    tempnoc = soup.find_all(attrs={'class': 'from'})
    for tempn in tempnoc:
        temp_n.append(tempn.text.split())

    panda = pandas.DataFrame({
        "Data": data,
        "Temperatura dzien": temp_d,
        "Temperatura noc": temp_n
    })
    print(panda)
    panda.to_excel("Temperatury.xlsx")
    Menu()

def Ksiezyc():
    JakoscDzisiaj = soup.find_all(attrs={'class': 'colorNoBold'})[3]
    print('Faza Księżyca to' , JakoscDzisiaj.text)
    Menu()

def Menu():
    menu = input('Co chcesz wyświetlić? 1. Temperaturę | 2. Faza księżyca |: ')
    if menu == '1':
        Temperatura()
    elif menu == '2':
        Ksiezyc()
    else:
        print('Wybrano niepoprawną akcję')
        Menu()
Menu()
