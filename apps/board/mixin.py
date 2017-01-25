from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class DefaultsMixin:
    """
    Whem authentication_classes is uncommented this bug appears

    NotImplementedError at /api/task/
    .authenticate() must be overridden.
    """
    # authentication_classes = (BaseAuthentication, TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
