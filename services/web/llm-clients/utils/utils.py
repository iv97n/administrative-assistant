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
    return doc["content"].decode('utf-8')
    """
    print(type(doc["content"]))
    if isinstance(type(doc["content"]), str):
          return doc["content"]
    """
    '''
    # doc = json.load(doc)
    """
    # Decode the base64 content
    binary_content = base64.b64decode(doc["content"])
    # Convert to a string (assuming UTF-8 encoding) and return it
    text_content = binary_content.decode("utf-8")
    text_content = html.unescape(text_content)
    """
    if doc['type'] != "text/html;charset=UTF-8":
        binary_content = ""
    else:
        binary_content = doc['content']

    
    return binary_content
    '''