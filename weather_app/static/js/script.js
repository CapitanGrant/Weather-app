document.getElementById('weather-form').addEventListener('submit', function(e) {
    e.preventDefault();
    let city = document.getElementById('city').value;

    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `city=${city}`
    })
    .then(response => response.json())
    .then(data => {
        let result = document.getElementById('weather-result');
        let city_name_locative = data.city_name_locative;
        let weather_data = data.weather_data;
        let weather_description = data.weather_description;

        result.innerHTML = `
            <h2>Погода в ${city_name_locative}</h2>
            <p>${weather_description}</p>
            <p>Температура: ${weather_data.current_weather.temperature}°C</p>
            <p>Ветер: ${weather_data.current_weather.windspeed} km/h</p>
        `;
    });
});