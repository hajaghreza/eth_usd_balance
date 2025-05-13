# main.py
import requests
from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.isConnected():
    print("Failed to connect to Ethereum node.")
    exit()

address = input("🔍 Enter Ethereum address: ")

if not w3.isAddress(address):
    print("Invalid address.")
    exit()

balance_wei = w3.eth.get_balance(address)
balance_eth = w3.fromWei(balance_wei, 'ether')

# Get ETH price
try:
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    price = response.json()["ethereum"]["usd"]
    balance_usd = float(balance_eth) * price
    print(f"💰 Balance of {address}: {balance_eth} ETH (~${balance_usd:.2f} USD)")
except Exception as e:
    print("Error fetching price:", e)
