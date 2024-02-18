import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining public IP: {e}")
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Your public IP address is: {public_ip}")
    else:
        print("Could not obtain public IP address. Please check your internet connection.")
