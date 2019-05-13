
import getpass
import random
import string
from user import User
from credentials import Credentials


def create_user(username, password1):
    '''
    Function to create new user
    '''
    new_user = User(username, password1)
    return new_user


def create_credentials(account_name, password):
    '''
    Function to create new account
    '''
    new_credentials = User(account_name, password)
    return new_credentials


def save_user(user):
    '''
    function to save user
    '''
    user.save_user()


def save_credentials(self):
    '''
    save_user method to save new users into the list
    '''
    Credentials.credentials_list.append(self)


def check_existing_user(password):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password)


def find_account(password):
    '''
    function to find account by its name
    '''
    return User.find_account(password)


def delete_credentials(self):
    '''
    delete method to delete saved information from the list
    '''
    Credentials.credentials_list.remove(self)


def display_credentials():
    '''
    method that returns the user list
    '''
    return User.display_users()


def james():
  print("Welcome to password locker")


def james1():
  print("Would you like to continue? (y/n)")
  answer = input()
  if answer == "yes":
    print("To continue press 1")
    one = input()
    if one == "1":
      print("Choose which you like to sign up/log in")
      print("Press x = sign up / Press y = log in / Press 1 = exit")
      logorsign = input()
      if logorsign == "x":
        print("Enter username.")
        username = input()
        print("Enter password.")
        password1 = getpass.getpass("password:")
        print("Confirm password")
        password2 = getpass.getpass("password:")
        if password1 == password2:
          print("New user: " + username + " created.")
          print("*****Choose log in this time.*****")
          save_user(create_user(username, password1))
          james1()
        else:
          print("Sorry passwords don't match.")
          james1()
      elif logorsign == "y":
        print("Enter Username.")
        username = input()
        print("Enter Password.")
        password3 = getpass.getpass("password:")
        if check_existing_user(password3):
          search_account = find_account(password3)
          if True:
            print(f"welcome  {search_account.username}")
            print("Press x = New credential. / Press y = View existing credentials / Press z = Delete credentials.")
            legacy = input()
            if legacy == "x":
              print("Enter account name.")
              account_name = input()
              print(
                  "Press 1 = New password / Press 2 = Make password.")
              passwrd = input()
              if passwrd == "1":
                letters = string.ascii_letters + string.digits
                genpassword = ''.join(random.choice(letters) for i in range(9))
                print(f"Your new generated password is: {genpassword}")
                password = genpassword
                print(f"{account_name} has been successfully saved")
                james1()
              elif passwrd == "1":
                print("Enter Password.")
                password = getpass.getpass("password:")
                print(f"{account_name} +  has been successfully saved")
                james1()
                save_credentials(create_credentials(account_name, password))
            elif legacy == "2":
              if display_credentials:
                print("Here is a list of all your accounts and passwords")
                for Credentials in display_credentials():
                  print(
                      f"Account name: {Credentials.account_name}  // password: {Credentials.password}")
              elif legacy == "3":
                print("Which credential would you like to delete?")
                delaccount = input()
                if delaccount == account_name:
                  Credentials.credentials_list.remove(Credentials)
                  print("Credential deleted")
                  james1()
                else:
                  print("No match")
                  james1()
        else:
          print("Incorrect username or password.Try again!")
          james1()
      elif logorsign == "3":
        exit()
    else:
      print("Press 1")
      james1()
  elif answer == "no":
    print("Thanks for using this application")
  else:
    print("Wrong choice.Try again!")
    james1()


if __name__ == '__main__':
  james()
  james1()
