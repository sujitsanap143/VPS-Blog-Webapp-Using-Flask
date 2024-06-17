from flask import current_app
from app import create_app
# or from yourapp import create_app
from app.models import Post
# If using create_app factory
app = create_app()
with app.app_context():
    Post.reindex()