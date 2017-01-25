from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView


class DefaultsMixin(APIView):
    authentication_classes = (BaseAuthentication, TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
