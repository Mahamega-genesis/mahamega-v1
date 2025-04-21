import requests

def fetch_volume_data(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=1"
    response = requests.get(url)
    data = response.json()

    volumes = data.get("total_volumes", [])
    if not volumes:
        return None

    # Ambil volume terakhir (terbaru)
    latest_volume = volumes[-1][1]
    return latest_volume
