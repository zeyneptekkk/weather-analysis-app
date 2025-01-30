
import requests
import json
import matplotlib.pyplot as plt
from termcolor import colored
import pyttsx3
sehir_ismi = input("Türkiyede hava durumunu öğrenmek istediğiniz şehri girin: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir_ismi},tr&APPID=228794b6179d9eb27cb0f491a2082f12"
sonuc = requests.get(url)

if sonuc.status_code == 200:
    sonuc_json = json.loads(sonuc.text)
    print("Şehir: " + str(sonuc_json["name"]))
    print("Ülke: " + str(sonuc_json["sys"]["country"]))
    print("Sıcaklık: " + str(round(sonuc_json["main"]["temp"] - 273, 2)) + "°C")
    print("Basınç: " + str(sonuc_json["main"]["pressure"]) + " Paskal")
    print("Nem Oranı: " + str(sonuc_json["main"]["humidity"]) + "%")
    print("Koordinatlar: " + str(sonuc_json["coord"]["lon"]) + " - " + str(sonuc_json["coord"]["lat"]))
else:
    print("Şehir bulunamadı veya bir hata oluştu.")

# Hava durumu ikonu
weather_icon = sonuc_json["weather"][0]["icon"]
icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"
print(colored("Hava Durumu İkonu: ", "blue", attrs=["bold"]) + icon_url)

# Emojiler
weather_main = sonuc_json["weather"][0]["main"]
if weather_main == "Clear":
    print(colored("Hava Durumu: ☀️", "yellow", attrs=["bold"]))
elif weather_main == "Rain":
    print(colored("Hava Durumu: 🌧️", "blue", attrs=["bold"]))
elif weather_main == "Clouds":
    print(colored("Hava Durumu: ☁️", "white", attrs=["bold"]))
else:
    print(colored("Hava Durumu: " + weather_main, "green", attrs=["bold"]))

# uyarılar
sicaklik = sonuc_json["main"]["temp"] - 273
if sicaklik > 30:
    print("⚠️ Sıcaklık çok yüksek! Dışarı çıkarken dikkatli olun.")
elif sicaklik < 10:
    print("⚠️ Sıcaklık çok düşük! Kalın giyinmeyi unutmayın.")

if "rain" in str(sonuc_json["weather"][0]["main"]).lower():
    print("🌧️ Yağmur yağacak! Yanınıza şemsiye alın.")

#hava durumunusesli oku
print("🎤 Hava durumu sesli söyleniyor....")
sesli = pyttsx3.init()
sesli.say(f"{sonuc_json['name']} şehrinde sıcaklık {round(sonuc_json['main']['temp'] - 273, 2)} derece.")
sesli.say(f"Hava durumu: {sonuc_json['weather'][0]['description']}.")
sesli.runAndWait()

