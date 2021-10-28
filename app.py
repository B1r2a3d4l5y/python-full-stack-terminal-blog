from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author="Brad",
            title="Sample title",
            description="Sample description",
            id="135")

blog.new_post()

blog.save_to_mongo()



print(blog.get_posts())
