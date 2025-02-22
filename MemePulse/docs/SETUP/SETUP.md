# Setup Instructions

1. **Install Python**: Ensure Python 3.9+ is installed.
2. **Install Dependencies**: Run `pip install -r requirements.txt`.
3. **Configure Environment**:
   - Copy `.env` template and fill in your keys:
     - X API credentials (from developer.x.com)
     - Solana RPC URL (e.g., Helius or public endpoint)
     - Helius API key (optional, for enhanced data)
     - Wallet private key (Base58 format, keep secure!)
4. **Run Tests**: `pytest tests/`
5. **Start the App**: `python src/main.py`