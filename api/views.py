from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import FavouritesSerializer, UserFavouritesSerializer
from .models import Favourites
from django.http import Http404


@api_view(['GET', 'POST'])
def check_if_email_exists(request):
    if request.method == 'GET':
        email = request.GET.get('email', None)
        user = get_object_or_404(User, email=email)
        if user is not Http404:
            data = {
                'user_id': str(user.id),
                'login_type': 'signin',
            }
            return Response(data)
        else:
            data = {
                'user_id': str(user.id),
                'login_type': 'signup',
            }
            return Response(data)
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            return Response({
                'message': 'login successful'
            })
        else:
            return Response({
                'message': 'failed'
            })
    else:
        return Response({'message': 'Use a legitimate request method'})
#
#
# @api_view(['POST'])
# def authenticate_credentials(request):
#     email = request.POST.get('email', None)
#     password = request.POST.get('password', None)
#     user = authenticate(email=email, password=password)
#     if user is not None:
#         return Response({
#             'message': 'login successful'
#         })
#     else:
#         return Response({
#             'message': 'failed'
#         })


@api_view(['POST'])
def register_new_user(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)

    user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
    return Response({
        'message': 'New user successfully registered',
    })


@api_view(['POST'])
def get_user_details(request):
    user_id = request.POST.get('user_id', None)
    user_object = get_object_or_404(User, id=user_id)
    serializer = UserFavouritesSerializer(user_object)
    return Response(serializer.data)


@api_view(['POST'])
def add_favourites_to_user(request):
    user_id = request.POST.get('user_id', None)
    fav = request.POST.get('favourite_category', None)
    user_obj = get_object_or_404(User, id=user_id)
    favourite_obj = Favourites.objects.create(user=user_obj, text=fav)
    return Response({'message': 'Successful'})


@api_view(['POST'])
def remove_favourites_from_user(request):
    user_id = request.POST.get('user_id', None)
    fav = request.POST.get('favourite_category', None)
    user_obj = get_object_or_404(User, id=user_id)
    favourite_obj = get_object_or_404(Favourites, user=user_obj, text=fav)
    favourite_obj.delete()
    return Response({'message': 'Successfully deleted'})
