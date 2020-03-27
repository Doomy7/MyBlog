from .models import users
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend

# custom Backend auth for users model
class UserBackend(ModelBackend):
    def authenticate(self, username, password):
        #check if input is email or username type
        test = username.split('@')
        if len(test) == 1:
            try:
                #if fetched check password
                check = users.objects.get(username=username)
                pwd_valid = check_password(password, check.password)
                #if password matched check if user is permitted to login
                #else return user is blocked
                if pwd_valid:
                    try:
                        user = User.objects.get(username=username)
                        return user
                    except:
                        return('User blocked')
                else:
                    return 'Wrong user or password'
            #if user not fetched user does not exist
            except users.DoesNotExist:
                return 'User does not exist'
        #the same applies below
        else:
            try:
                user = users.objects.get(email=username)
                pwd_valid = check_password(password, user.password)
                if pwd_valid:
                    try:
                        user = User.objects.get(email=username)
                        return user
                    except:
                        return('User blocked')
                else:
                    return 'Wrong user or password'
            except users.DoesNotExist:
                return 'User does not exist'
