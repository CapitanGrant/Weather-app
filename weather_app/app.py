from flask import Flask, render_template, request, jsonify, session
import os
import pymorphy3
from aiohttp import ClientSession

app = Flask(__name__)
app.secret_key = os.urandom(24)
morph = pymorphy3.MorphAnalyzer()

API_URL = "https://api.open-meteo.com/v1/forecast"

weather_code_descriptions = {
    0: "Небо ясное",
    1: "В основном ясно",
    2: "Переменная облачность",
    3: "Пасмурно",
    45: "Туман",
    48: "Образуется иней",
    51: "Морось: слабая",
    53: "Морось: Умеренная",
    55: "Морось: Сильная",
    56: "Морось: слабая",
    57: "Морось: сильная",
    61: "Дождь: Слабый",
    63: "Дождь: Умеренный",
    65: "Дождь: Большой интенсивности",
    66: "Ледяной дождь: Небольшой",
    67: "Ледяной дождь: Большой интенсивности",
    71: "Снегопад: Небольшой",
    73: "Снегопад: Умеренный",
    75: "Снегопад: Интенсивный",
    77: "Снежная крупа",
    80: "Ливни: Незначительные",
    81: "Ливни: Умеренные",
    82: "Ливни: сильные",
    85: "Снегопады: Незначительные",
    86: "Снегопады: Сильные",
    95: "Гроза: слабая или умеренная",
    96: "Гроза с небольшим градом",
    99: "Гроза с сильным градом"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    history = session.get('history', [])
    return jsonify(history)


@app.route('/stats')
def stats():
    from collections import Counter
    history = session.get('history', [])
    stats = Counter(history)
    return jsonify(stats)


async def get_coordinates(city):
    geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key=2f96942a6c5e43929f6fbecb1e51071e"
    async with ClientSession() as session_client:
        async with session_client.get(geocode_url) as response:
            weather_json = await response.json()
            if weather_json['results']:
                lat = weather_json['results'][0]['geometry']['lat']
                lng = weather_json['results'][0]['geometry']['lng']
                return lat, lng
            return None, None


def get_first_word_before_comma(input_string):
    parts = input_string.split(',')
    return parts[0].strip()


def decline_city_name(city_name, case):
    morph = pymorphy3.MorphAnalyzer()
    parsed_city = morph.parse(city_name)[0]
    return parsed_city.inflect({case}).word


@app.route('/weather', methods=['POST'])
async def get_weather():
    city = request.form['city']
    parsed_city = morph.parse(city)[0]
    city_name_clean = get_first_word_before_comma(parsed_city.word)
    city_name_locative = decline_city_name(city_name_clean, 'loct').title()
    lat, lon = await get_coordinates(city)
    if lat is None or lon is None:
        return jsonify({'error': 'City not found'}), 404

    async with ClientSession() as session_client:
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': 'true'
        }
        async with session_client.get(url=API_URL, params=params) as response:
            weather_data = await response.json()
            if 'history' not in session:
                session['history'] = []
            session['history'].append(city)
            session.modified = True
            weather_description = weather_code_descriptions.get(weather_data['current_weather']['weathercode'],
                                                                "Unknown")

    return jsonify({
        'city_name_locative': city_name_locative,
        'weather_data': weather_data,
        'weather_description': weather_description
    })


if __name__ == '__main__':
    app.run(debug=True)
