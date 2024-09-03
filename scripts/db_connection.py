from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb+srv://ahadfardinpen:327346cse@cluster0.um0bk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    return client['upchecker']
