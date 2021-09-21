# my_app/authentication.py
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from user.models import UserApipermissions,UserUserattribute
from .variables import view_to_obj
class SpecialAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        username = request.META.get('X_USERNAME') # get the username request header
        if not username: # no username passed in request headers
            return None # authentication did not succeed

        try:
            user = User.objects.get(username=username) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, None) # authentication successful

    def has_permission(self, request, view):
        if not str(request.user) == "AnonymousUser":
            user_attr = UserUserattribute.objects.get(user=request.user)
            if user_attr.api_login or user_attr.full_api_login:
                view_name = view_to_obj[view.__class__.__name__]
                api_permission = UserApipermissions.objects.get(api=user_attr)
                if getattr(api_permission,view_name):
                    return bool(request.user and request.user.is_authenticated)
        else:
            return False
        