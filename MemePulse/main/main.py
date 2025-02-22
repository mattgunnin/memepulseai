from ai.sentiment import SentimentAnalyzer, fetch_x_posts
from ai.scoring_model import MemecoinScorer
from blockchain.solana_client import SolanaClient
from blockchain.sniper import Sniper
from api.x_api import get_x_credentials
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    sentiment_analyzer = SentimentAnalyzer()
    scorer = MemecoinScorer()
    solana_client = SolanaClient(os.getenv("SOLANA_RPC_URL"), os.getenv("WALLET_PRIVATE_KEY"))
    sniper = Sniper(solana_client)

    x_creds = get_x_credentials()
    tweets = fetch_x_posts(**x_creds, query="solana memecoin")
    avg_sentiment = sum(sentiment_analyzer.analyze(tweet)["score"] for tweet in tweets) / len(tweets)

    token_address = "ExampleTokenAddress"
    token_data = solana_client.get_token_data(token_address)
    
    hype_score = scorer.score(avg_sentiment, token_data["volume"], token_data["liquidity"])
    print(f"Hype Score for {token_address}: {hype_score:.2f}")

    if hype_score > 0.7:
        sniper.execute_trade(token_address, 0.1)

if __name__ == "__main__":
    main()