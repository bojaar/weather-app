# 🌤 Weather App

Prosta aplikacja desktopowa do sprawdzania aktualnej pogody w Pythonie z wykorzystaniem biblioteki Tkinter oraz darmowego API Open-Meteo.

---

## Autor

Daniel Bojarski

---

## Opis projektu

Aplikacja umożliwia sprawdzenie aktualnej pogody dla wybranego miasta.

Po wpisaniu nazwy miasta użytkownik otrzymuje informacje o:

- temperaturze,
- temperaturze odczuwalnej,
- wilgotności,
- prędkości wiatru,
- ciśnieniu atmosferycznym,
- godzinie ostatniej aktualizacji.

Dodatkowo aplikacja zapamiętuje historię ostatnich wyszukiwań.

---

## Wykorzystane technologie

- Python 3
- Tkinter
- Requests
- Open-Meteo API

---

## Struktura projektu

```
weather-app/
│
├── main.py
├── weather.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/bojaar/weather-app.git
```

2. Przejdź do folderu projektu:

cd weather-app

3. Zainstaluj wymagane biblioteki:

pip install -r requirements.txt

---

## Uruchomienie

Uruchom aplikację poleceniem:

python main.py

---

## Funkcje aplikacji

- wyszukiwanie pogody dla miasta,
- wyświetlanie aktualnej temperatury,
- temperatura odczuwalna,
- wilgotność powietrza,
- prędkość wiatru,
- ciśnienie atmosferyczne,
- historia wyszukiwań,
- data i godzina ostatniej aktualizacji,
- obsługa błędów.

---

## Źródło danych

Aplikacja korzysta z darmowego API:

https://open-meteo.com/

---

## Licencja

Projekt został przygotowany w celach edukacyjnych.