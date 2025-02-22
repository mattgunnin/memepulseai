class MemecoinScorer:
    def __init__(self):
        self.weights = {"sentiment": 0.4, "volume": 0.3, "liquidity": 0.3}

    def score(self, sentiment_score, volume, liquidity):
        normalized_volume = min(volume / 1000000, 1)  # Normalize to SOL units
        normalized_liquidity = min(liquidity / 500000, 1)
        total_score = (
            self.weights["sentiment"] * sentiment_score +
            self.weights["volume"] * normalized_volume +
            self.weights["liquidity"] * normalized_liquidity
        )
        return min(total_score, 1)  # Cap at 1