from src.ai.sentiment import SentimentAnalyzer

def test_sentiment_analysis():
    analyzer = SentimentAnalyzer()
    result = analyzer.analyze("This memecoin is awesome!")
    assert result["label"] in ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    assert 0 <= result["score"] <= 1