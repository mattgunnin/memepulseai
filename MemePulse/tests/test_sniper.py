from src.blockchain.solana_client import SolanaClient
from src.blockchain.sniper import Sniper

def test_sniper_init():
    client = SolanaClient("https://api.mainnet-beta.solana.com", "fake_private_key")
    sniper = Sniper(client)
    assert sniper.client == client