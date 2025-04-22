import os
import json
from pymongo import MongoClient

# Connect to MongoDB
# Your IP address must be whitelisted in the MongoDB Atlas cluster first. 
client = MongoClient(os.getenv("MONGODB_BRIGHTGAUGE_URI"))

# Connect to the database
db = client["ninja"]

# Connect to the collection 'devices'
collection = db["devices"]

# Get all documents in the collection to a list
mongo_results = collection.find()
documents = list(mongo_results)