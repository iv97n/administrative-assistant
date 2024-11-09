from pymongo import MongoClient
import base64
import html
import json


def retrieve_documents(mongo_uri, mongo_db, mongo_collection):
        client = MongoClient(mongo_uri)
        db = client[mongo_db]      
        collection = db[mongo_collection]  
        
        for doc in collection.find():
                yield doc


def parse_document(doc):
    doc = json.load(doc)
    # Decode the base64 content
    binary_content = base64.b64decode(doc["content"]["$binary"]["base64"])
    # Convert to a string (assuming UTF-8 encoding) and return it
    text_content = binary_content.decode("utf-8")
    text_content = html.unescape(text_content)
    
    return text_content