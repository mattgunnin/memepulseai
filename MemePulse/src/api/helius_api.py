import requests
import os

def get_token_metrics(token_address):
    api_key = os.getenv("HELIUS_API_KEY")
    url = f"https://api.helius.xyz/v0/tokens/{token_address}?api-key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"volume": 0, "liquidity": 0}  # Fallback