from rest_framework import authentication
from rest_framework import permissions


class DefaultsMixin:
    authentication_classes = (
        authentication.BaseAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated, )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100