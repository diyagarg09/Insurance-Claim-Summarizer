from pymongo import MongoClient

# MongoDB connection setup
# 'localhost' tab use karein agar MongoDB aapke computer par installed hai
client = MongoClient("mongodb://localhost:27017/")
db = client["insurance_db"]
collection = db["claim_summaries"]

def save_to_db(claim_data):
    """Summaries aur metadata ko DB mein save karne ke liye"""
    result = collection.insert_one(claim_data)
    return str(result.inserted_id)