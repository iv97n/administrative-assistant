from pymongo import MongoClient


def retrieve_documents(mongo_uri, mongo_db, mongo_collection):
        client = MongoClient(mongo_uri)
        db = client[mongo_db]      
        collection = db[mongo_collection]  
        
        for doc in collection.find():
                yield doc
