import firebase_admin
from google.cloud import firestore


# Firestoreデータベースの参照
db = firestore.client()

def get_trade_posts():
    """Firestoreからトレード掲示板の投稿を取得"""
    posts_ref = db.collection('trade_posts')
    docs = posts_ref.stream()
    posts = []
    for doc in docs:
        posts.append(doc.to_dict())
    return posts

def add_trade_post(title, description, user_name, get_card):
    """新しいトレード投稿をFirestoreに追加"""
    posts_ref = db.collection('trade_posts')
    post_data = {
        'title': title,
        'description': description,
        'user_name': user_name,
        'get_card': get_card,
        'created_at': firestore.SERVER_TIMESTAMP
    }
    posts_ref.add(post_data)
