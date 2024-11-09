from clients.salamandra_client import SalamandraClient
import os
from dotenv import load_dotenv

from utils.utils import retrieve_documents
load_dotenv()

"""

file_path = './src/summarizer/data/finetune.txt'


with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


client = SalamandraClient()
instrucció = "Es pot reconèixer pel b2 de català?"

print(client.give_prediction(instrucció, file_content))

"""
for document in retrieve_documents(os.getenv('MONGO_URI'), os.getenv('MONGO_DATABASE'), os.getenv('MONGO_COLLECTION')):
    print(document)
