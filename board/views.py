from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from . models import Sprint, Task
from rest_framework.authtoken.models import Token
from . serializers import Sprinterserializers, Userserializer, Taskserializer
User = get_user_model()

class DefaultsMixin(object):
    authentication_classes = (
        authentication.BaseAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated
    )
    pagenate_by = 5
    pagenate_by_param = 'page_size'
    max_paginated_by = 100

class Sprintviewsets( DefaultsMixin, viewsets.ModelViewSet):
    user = get_user_model().objects.first()
    token = Token.objects.create(user=user)
    queryset  = Sprint.objects.order_by("end")
    serializer_class = Sprinterserializers

class Taskviewset(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Taskserializer

class Userviewset(DefaultsMixin, viewsets.ModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = Userserializer


