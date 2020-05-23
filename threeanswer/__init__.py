import pymongo
import pprint
import logging
import json
import azure.functions as func

from pymongo import MongoClient

# Initialize the Cosmos client
client = MongoClient('mongodb://familyfeuddb:yNfFMBhN6MUGAOgusJzoyviFVKQweWuS2gPzHnoioE2NdZ3xpkhkb7Grm6fzYkzLK3Ke2Hd3ESl8Uinarl5AWw==@familyfeuddb.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    db = client['familyfeuddb']
    collection = db.collection_names()
    for collect in collection:
        pprint.pprint(collect)

    return func.HttpResponse(f"Hello {collection[0]}!")
