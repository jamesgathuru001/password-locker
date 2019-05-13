
from credentials import Credentials


class User:
    """
    Class that generates new users
    """
    user_list = []

    def __init__(self, username, password):
      self.username = username
      self.password = password

    def save_user(self):
        '''
        save_user method to save new users into the list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete method to delete saved user from list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def user_exist(cls, password):
        '''
        method to check if a user and
        their details exist
        '''
        for user in cls.user_list:
            if user.password == password:
                return True
        return False

    @classmethod
    def find_account(cls, password):
        '''
        method that finds an account by its name
        '''
        for user in cls.user_list:
            if user.password == password:
                return user
