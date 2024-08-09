from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.db.models.signals import pre_init
from django.dispatch import receiver



# reciever function 
# def login_done(sender,request,user,**kwargs):
#     print('I am logged in Signals')
#     print(f'User: {user}')
#     print(f'Request: {request}')
#     print(f'kwargs: {kwargs}')
#     print(sender)
#     # I want to send an email whenever someone login into my system.

# user_logged_in.connect(login_done, sender=User)
# signal.connect(rec_func , sender)


# @receiver(user_logged_out,sender=User)
# def logout_done(sender,request,user,**kwargs):
#     print('I am logged out Signals')
#     print(f'User: {user}')
#     print(f'Request: {request}')
#     print(f'kwargs: {kwargs}')
#     print(sender)

# @receiver(user_login_failed)
# def login_failed(sender,request,credentials,**kwargs):
#     print('I am logged in failed Signals')
#     print(f'Request: {request}')
#     print(f'Credentials: {credentials}')
#     print(f'kwargs: {kwargs}')
#     print(sender)

# @receiver(pre_init, sender=User)
# def before_interaction_with_models(sender,*args,**kwargs):
#     print('I am before interaction with models Signals')
#     print(f'Sender: {sender}')
#     print(f'Args: {args}')
#     print(f'kwargs: {kwargs}')
