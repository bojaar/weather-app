import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from weather import get_weather


BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2d2d44"
TEXT_COLOR = "#ffffff"
SECONDARY_TEXT = "#b8b8d1"
BUTTON_COLOR = "#4f8cff"


history = []


def search_weather():
    """Pobiera pogodę dla wpisanego miasta i aktualizuje interfejs."""

    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Błąd", "Podaj nazwę miasta!")
        return

    try:
        weather = get_weather(city)

        city_label.config(text=f"📍 {weather['city']}")
        temp_label.config(text=f"{weather['temperature']}°C")

        details_label.config(
            text=(
                f"🤗 Odczuwalna: {weather['feels_like']}°C\n"
                f"💧 Wilgotność: {weather['humidity']}%\n"
                f"🌬 Wiatr: {weather['wind']} km/h\n"
                f"🌡 Ciśnienie: {weather['pressure']} hPa"
            )
        )

        time_label.config(
            text=f"Ostatnia aktualizacja: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        )

        add_to_history(weather["city"])

    except Exception as error:
        messagebox.showerror("Błąd", str(error))


def add_to_history(city):
    """Dodaje miasto do historii wyszukiwań."""

    if city in history:
        history.remove(city)

    history.insert(0, city)

    if len(history) > 5:
        history.pop()

    update_history_label()


def update_history_label():
    """Aktualizuje tekst z historią wyszukiwań."""

    if not history:
        history_label.config(text="Brak historii wyszukiwań.")
        return

    text = "Ostatnie wyszukiwania:\n" + "\n".join(f"• {city}" for city in history)
    history_label.config(text=text)


def search_on_enter(event):
    """Uruchamia wyszukiwanie po naciśnięciu klawisza Enter."""

    search_weather()


root = tk.Tk()
root.title("Weather App")
root.geometry("520x700")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 26, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root,
    text="Aplikacja pogodowa w Pythonie i Tkinter",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg=SECONDARY_TEXT,
)
subtitle_label.pack()

search_frame = tk.Frame(root, bg=BG_COLOR)
search_frame.pack(pady=20)

city_entry = tk.Entry(
    search_frame,
    font=("Arial", 14),
    width=24,
)
city_entry.grid(row=0, column=0, padx=5)
city_entry.bind("<Return>", search_on_enter)

search_button = tk.Button(
    search_frame,
    text="Szukaj",
    font=("Arial", 12, "bold"),
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    width=10,
    command=search_weather,
)
search_button.grid(row=0, column=1, padx=5)

weather_card = tk.Frame(
    root,
    bg=CARD_COLOR,
    width=420,
    height=360,
)
weather_card.pack(pady=15)
weather_card.pack_propagate(False)

city_label = tk.Label(
    weather_card,
    text="Wpisz nazwę miasta",
    font=("Arial", 18, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
)
city_label.pack(pady=25)

temp_label = tk.Label(
    weather_card,
    text="--°C",
    font=("Arial", 42, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
)
temp_label.pack(pady=10)

details_label = tk.Label(
    weather_card,
    text="Tutaj pojawią się dane pogodowe.",
    font=("Arial", 14),
    bg=CARD_COLOR,
    fg=SECONDARY_TEXT,
    justify="left",
)
details_label.pack(pady=15)

time_label = tk.Label(
    weather_card,
    text="",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg=SECONDARY_TEXT,
)
time_label.pack(pady=10)

history_card = tk.Frame(
    root,
    bg=CARD_COLOR,
    width=420,
    height=130,
)
history_card.pack(pady=10)
history_card.pack_propagate(False)

history_label = tk.Label(
    history_card,
    text="Brak historii wyszukiwań.",
    font=("Arial", 12),
    bg=CARD_COLOR,
    fg=SECONDARY_TEXT,
    justify="left",
)
history_label.pack(pady=15)

root.mainloop()