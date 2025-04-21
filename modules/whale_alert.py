import requests

API_URL = "https://api.cryptocurrencyalerting.com/v1/alerts"
API_KEY = "ZPDZJWuZ9SpqMOGbygpuQ2HCF607q5"  # ganti dengan API key kamu

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_whale_data(coin):
    try:
        response = requests.get(API_URL, headers=headers, params={"coin": coin})
        if response.status_code == 200:
            data = response.json()
            return data.get("alerts", [])
        else:
            return f"Whale alert error: {response.status_code}"
    except Exception as e:
        return f"Whale alert exception: {str(e)}"
