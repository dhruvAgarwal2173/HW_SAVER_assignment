from django.urls import path
from .views import *


urlpatterns = [
    path('check-user/', check_if_email_exists, name='check-user'),
    path('register-user/', register_new_user, name='register-user'),
    path('user-details/', get_user_details, name='user-details'),
    path('add-favourite/', add_favourites_to_user, name='add-favourite'),
    path('remove-favourite', remove_favourites_from_user, name='remove-favourite'),
]