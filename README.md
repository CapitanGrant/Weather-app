# Flask Weather App

This is a Flask-based web application that provides weather information for a given city using the Open-Meteo API. The application also keeps track of search history and provides basic statistics.

## Features

- Get current weather information for a specified city.
- View search history.
- View basic statistics on searched cities.
- Properly handles city name declension in Russian for better user experience.

## Requirements

- Python 3.x
- Flask
- Requests
- Pymorphy2

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Ensure you have an API key for OpenCage Geocoding API. Replace the placeholder key in the `get_coordinates` function with your actual API key:
```python
geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key=YOUR_API_KEY"
