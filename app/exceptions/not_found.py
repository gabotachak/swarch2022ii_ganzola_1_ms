class NotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class UserNotFoundException(NotFoundException):
    def __init__(self, user: str = None):
        self.resource = "User"
        self.resource_id = user
