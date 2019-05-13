
class Credentials:
    '''
    class that generates new credentials intsances
    '''

    credentials_list = []

    def __init__(self, account_name, password):
        '''
        init method to create instances of the credentials class
        '''
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        save_user method to save new users into the list
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def delete_credentials(cls, account_name, password):
        '''
        delete method to delete saved user from list
        '''
        for Credentials in cls.credentials_list:
          if Credentials.account_name == account_name:
            return Credentials

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.credentials_list
