from database import Database
from models.post import Post

Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            content="This is some sample content",
            author="Brad")

post_save_to_mongo()
