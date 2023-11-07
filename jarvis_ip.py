import requests

def get_public_ip():
    """Get the current public IP address of the user."""
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to get IP address")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None