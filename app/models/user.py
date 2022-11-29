class User:
    id_user: str
    first_name: str
    last_name: str
    username: str

    class Meta:
        table_name = "user"
        fields = ("id_user", "first_name", "last_name", "username")

    def __init__(
            self,
            id_user: int = None,
            first_name: str = None,
            last_name: str = None,
            username: str = None
    ):
        self.id_user = id_user
        self.first_name = first_name.title() if first_name else None
        self.last_name = last_name.title() if last_name else None
        self.username = username.lower() if username else None

    def to_dict(self):
        return {
            "id_user": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username
        }

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.id_user == other.id_user
