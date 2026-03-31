from models.domain_models import User, Location
from .base_repository import BaseRepository


class UserRepository(BaseRepository):

    def login(self, email, password_hash):
        query = "SELECT * FROM users WHERE email=%s AND password_hash=%s"
        row = self.fetch_one(query, (email, password_hash))
        if not row:
            return None

        location = Location(row["location_id"], "", "")
        return User(row["user_id"],
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["role"],
                    location)