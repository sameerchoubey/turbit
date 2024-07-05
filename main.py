from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# MongoDB connection details
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['jsonplaceholder']
posts_collection = db['posts']
comments_collection = db['comments']
users_collection = db['users']

@app.get("/posts")
def get_all_posts():
    print('http://localhost:8000/posts')
    posts = list(posts_collection.find())
    for post in posts:
        post['_id'] = str(post['_id'])
    return posts

@app.get("/comments")
def get_all_comments():
    comments = list(comments_collection.find())
    for comment in comments:
        comment['_id'] = str(comment['_id'])
    return comments

@app.get("/users")
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return users

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int):
    posts = list(posts_collection.find({"userId": user_id}))
    if not posts:
        raise HTTPException(status_code=404, detail="User or posts not found")
    for post in posts:
        post['_id'] = str(post['_id'])

    res = {
        "count": len(posts),
        "total_posts": posts
    }
    return res

@app.get("/posts/{post_id}/comments")
def get_post_comments(post_id: int):
    comments = list(comments_collection.find({"postId": post_id}))
    if not comments:
        raise HTTPException(status_code=404, detail="Post or comments not found")
    for comment in comments:
        comment['_id'] = str(comment['_id'])

    res = {
        "count": len(comments),
        "total_comments": comments
    }
    return res

@app.post("/users")
def create_user(user: dict):
    result = users_collection.insert_one(user)
    user['_id'] = str(result.inserted_id)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: str, user: dict):
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    user['_id'] = user_id
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "User deleted successfully"}
