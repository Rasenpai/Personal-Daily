import requests as req
from colorama import Fore, Style, init
import os

init(autoreset=True)

# Konstanta API
WEATHER_API_KEY = "b08546b699004229beeaac591d87a077"
GNEWS_API_KEY = "670f878a5f07a4d2c55f6aa591c2042f"
QUOTES_API_URL = "https://zenquotes.io/api/random"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
    response = req.get(url)
    return response.json() if response.status_code == 200 else None


def get_weather_emoji(icon):
    if "01" in icon:
        return "☀️"
    elif "02" in icon or "03" in icon:
        return "⛅"
    elif "04" in icon:
        return "☁️"
    elif "09" in icon or "10" in icon:
        return "🌧️"
    elif "11" in icon:
        return "⛈️"
    elif "13" in icon:
        return "❄️"
    else:
        return "🌫️"


def get_news(country_code):
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country={country_code.lower()}&topic=technology&token={GNEWS_API_KEY}"
    response = req.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])[:3]
    return None


def get_quote():
    response = req.get(QUOTES_API_URL)
    if response.status_code == 200:
        data = response.json()
        return f'{data[0]["q"]} - {data[0]["a"]}'
    return "No quote found."


def show_dashboard(city):
    weather_data = get_weather_data(city)
    if not weather_data:
        print(Fore.RED + f"❌ Kota tidak ditemukan atau kesalahan jaringan.")
        return

    # Weather data
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind = weather_data["wind"]["speed"]
    desc = weather_data["weather"][0]["description"].capitalize()
    icon = weather_data["weather"][0]["icon"]
    emoji = get_weather_emoji(icon)

    # News & Quote
    news = get_news(country)
    quote = get_quote()

    # Display output
    print(Fore.YELLOW + "\n" + "=" * 40)
    print(Fore.CYAN + f"{'Personal Daily Dashboard':^40}")
    print(Fore.YELLOW + "=" * 40)

    print(Fore.GREEN + f"📍 Lokasi     : {city_name}, {country}")
    print(Fore.YELLOW + f"🌡️  Suhu      : {temp}°C (Feels like {feels_like}°C)")
    print(Fore.MAGENTA + f"☁️  Cuaca     : {desc} {emoji}")
    print(Fore.BLUE + f"💧 Kelembapan : {humidity}%")
    print(Fore.WHITE + f"🌬️  Angin     : {wind} m/s")
    print(Fore.YELLOW + "=" * 40)

    print(Fore.CYAN + "📰 Berita Teknologi:")
    if news:
        for i, article in enumerate(news, 1):
            print(f"{i}. {article['title']}\n   {article['url']}\n")
    else:
        print("Tidak ada berita teknologi ditemukan.")

    print(Fore.YELLOW + "=" * 40)
    print(Fore.GREEN + "💬 Quote of the Day:")
    print(Fore.WHITE + f'"{quote}"')
    print(Style.RESET_ALL + "=" * 40)


# Main
if __name__ == "__main__":
    clear_screen()
    city_input = input(Fore.CYAN + "Masukkan nama kota: ").lower()
    show_dashboard(city_input)
