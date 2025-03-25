from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, name, email, role):
        self._id = id
        self._name = name
        self._email = email
        self._role = role


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def role(self):
        return self._role
    
    """
    Må implementeres om vi ikke bruker UserMixin fra flask_login

    def is_authenticated(self)

    def is_active(self)
    
    def is_anonymous(self)

    def get_id()
    
    """
    



