class User:
    def __init__(
        self,
        id: int,
        username: str,
        email: str,
        level: str,
        created_at: str,
        updated_at: str,
    ):
        self.id = id
        self.username = username
        self.email = email
        self.level = level
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"
