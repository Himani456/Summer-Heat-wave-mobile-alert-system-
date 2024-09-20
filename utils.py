import requests
import json

def get_temperature_data(api_url, api_key):
    """Fetch current temperature data from a weather API."""
    try:
        response = requests.get(api_url, params={'apikey': api_key})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get('current', {}).get('temperature')
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
        return None

def is_heat_wave(current_temp, threshold_temp):
    """Determine if the current temperature exceeds the heat wave threshold."""
    return current_temp >= threshold_temp

def load_config(config_path):
    """Load configuration settings from a JSON file."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def send_notification(message):
    """Placeholder function to send notifications."""
    # Here, implement your notification logic (e.g., using push notifications)
    print(f"Notification: {message}")
