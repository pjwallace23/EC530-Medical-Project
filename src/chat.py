from pymongo import MongoClient
import json

def add_user(self, first, last, uid):
    client = MongoClient("mongodb+srv://peterjw:Jarhg67Busd@cluster0.oezzd.mongodb.net/pmc-ec530?retryWrites=true&w=majority")
    users_collection = client.get_collection("users")
    users_collection.insert_one({'first':first,'last':kast,'id':uid})
    return 1

def send_message(self, sender_id:str, recipient_id:str, message:str):
    client = MongoClient("mongodb+srv://peterjw:Jarhg67Busd@cluster0.oezzd.mongodb.net/pmc-ec530?retryWrites=true&w=majority")
    messages_collection = client.get_collection("messages")
    messages_collection.insert_one({'sender_id':sender_id, 'recipient_id':recipient_id, 'message':message})
    return 1

def get_id(self, first, last):
    client = MongoClient("mongodb+srv://peterjw:Jarhg67Busd@cluster0.oezzd.mongodb.net/pmc-ec530?retryWrites=true&w=majority")
    users_collection = client.get_collection("users")
    my_query = {'first': first, 'last': last}
    my_entry = users_collection.find(my_query)
    return my_entry['id']

def get_messages_received(self, first, last):
    client = MongoClient("mongodb+srv://peterjw:Jarhg67Busd@cluster0.oezzd.mongodb.net/pmc-ec530?retryWrites=true&w=majority")
    messages_collection = client.get_collection("messages")
    search_id = get_id(first, last)
    return messages_collection.find({'id': search_id})





