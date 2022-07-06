import os


class Config:
    BTC_NODE_HOST = os.getenv("BTC_NODE_HOST", f"http://username:password@host:port")
    WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "...")
