__author__ = 'remillet'

from django.contrib.auth.models import User, UserManager, AbstractUser

class CSpaceAuthN(object):
    authNDictionary = dict()

    def authenticateWithCSpace(self, username=None, password=None):
        return True;

    def authenticate(self, username=None, password=None):
    # Check the username/password and return a User.
        authenticatedWithCSpace = self.authenticateWithCSpace(username=username, password=password)
        if authenticatedWithCSpace:
            try:
                newUser = User.objects.get(username=username)
                newUser.cspace_password = password
                self.authNDictionary[username] = password
                return newUser
            except User.DoesNotExist:
                newUser = User(username=username, password='none')
                newUser.cspace_password = password
                newUser.is_staff = True
                newUser.is_superuser = True
                newUser.save()
                self.authNDictionary[username] = password
                return newUser
        else:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            username = user.username
            passwd = self.authNDictionary[username];
            user.cspace_password = passwd
        except User.DoesNotExist:
            return None
        return user