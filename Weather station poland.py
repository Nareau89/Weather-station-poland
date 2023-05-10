import json
import requests

request = requests.get("https://danepubliczne.imgw.pl/api/data/synop/")
cities = request.json()

def wind_direction(degree):
    if degree >= 0 and degree <= 22 or degree > 337 and degree >= 359:
        return "północny"
    elif degree > 22 and degree <= 67 :
        return "północno-wschodni"
    elif degree > 67 and degree <= 112:
        return "wschodni"
    elif degree > 112 and degree <= 157:
        return "południowo-wschodni"
    elif degree > 157 and degree <= 202:
        return "południowy"
    elif degree > 202 and degree <= 247:
        return "południowo-zachodni"
    elif degree > 247 and degree <= 292:
        return "zachodni"
    elif degree > 292 and degree <= 337:
        return "północno-zachodni"
    else:
        return "brak danych"

stationList = []

for stations in cities:
    stationList.append(stations["stacja"])

print(stationList)

while (True):
    answer = input("Wybierz stacje: ").title()
    for stations in cities:
        if stations["stacja"] == answer:
            print("")
            print("nazwa stacji:", stations["stacja"])
            print("data pomiaru:", stations["data_pomiaru"].replace("None", "brak danych"))
            print("godzina pomiaru:", stations["godzina_pomiaru"].replace("None", "brak danych"))
            print("temperatura:", stations["temperatura"].replace("None", "brak danych"), "℃")
            print("prędkość wiatru:", stations["predkosc_wiatru"].replace("None", "brak danych"), "km/h")
            print("kierunek wiatru:", wind_direction(int(stations["kierunek_wiatru"])))
            print("wilgotnosc względna:", stations["wilgotnosc_wzgledna"].replace("None", "brak danych"),"%")
            print("suma opadu:", stations["suma_opadu"].replace("None", "brak danych"), "mm")
            print("ciśnienie:", str(stations["cisnienie"]).replace("None", "brak danych"), "hPa")
            print("")
            print(stationList)
