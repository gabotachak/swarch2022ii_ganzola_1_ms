class AlreadyExistsException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class UserAlreadyExistsException(AlreadyExistsException):
    def __init__(self, user=None):
        self.resource = "User"
        self.resource_id = user
