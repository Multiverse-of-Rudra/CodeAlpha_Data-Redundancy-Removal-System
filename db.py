from pymongo import MongoClient
from urllib.parse import quote_plus

# Encode credentials to safely include special characters
username = quote_plus("Rudra_123")
password = quote_plus("Rudra@32")

# Replace 'rudra.r58g27m.mongodb.net' with your actual cluster host if different
uri = f"mongodb+srv://{username}:{password}@rudra.r58g27m.mongodb.net/"

# Initialize the MongoDB client
client = MongoClient(uri)

# Connect to database and collection
db = client["data_cleaning"]
collection = db["entries"]

def fetch_existing_hashes():
    """Fetch all existing data hashes from the database"""
    return set(item["hash"] for item in collection.find({}, {"hash": 1}))

def insert_data(data: str, hash_val: str):
    """Insert new data and its hash into the database"""
    collection.insert_one({"data": data, "hash": hash_val})
