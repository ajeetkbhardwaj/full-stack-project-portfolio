from fastapiworkflow.schemas.post import Post
from fastapiworkflow.schemas.user import User

class DummyDatabase:
    users: dict[int, User] = {}
    posts: dict[int, Post] = {}


db = DummyDatabase()