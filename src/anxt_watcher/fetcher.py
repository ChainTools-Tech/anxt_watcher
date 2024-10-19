import requests
from tqdm import tqdm


def fetch_data(host):
    url_http = f"http://{host}/nxt?requestType=getState"
    url_https = f"https://{host}/nxt?requestType=getState"

    try:
        tqdm.write(f"Trying http for {host}")
        response = requests.get(url_http, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        tqdm.write(f"http failed, trying https for {host}")
        try:
            response = requests.get(url_https, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            tqdm.write(f"Error fetching data from {host}: {e}")
            return None
