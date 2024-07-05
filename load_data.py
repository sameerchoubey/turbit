import requests
from pymongo import MongoClient

# MongoDB connection details
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['jsonplaceholder']
posts_collection = db['posts']
comments_collection = db['comments']

# Fetch data from the API
posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')

# Store data in MongoDB
if posts_response.status_code == 200:
    posts = posts_response.json()
    posts_collection.insert_many(posts)
    print("Posts data inserted into MongoDB")

if comments_response.status_code == 200:
    comments = comments_response.json()
    comments_collection.insert_many(comments)
    print("Comments data inserted into MongoDB")

mongo_client.close()