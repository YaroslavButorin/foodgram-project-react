from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from api.pagination import LimitPageNumberPagination
# from api.serializers import FollowSerializer
from users.models import Follow

User = get_user_model()