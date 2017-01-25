from datetime import date
from django.utils.translation import ugettext_lazy
from rest_framework import serializers
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


class ValidatorMixin:

    def check_if_is_not_finished(self):
        if self.instance.status == Task.STATUS_DONE:
            show_error('Cannot change the sprint of a completed task')

    def check_if_is_not_a_old_sprint(self, value, message):
        if value and value.end < date.today():
            show_error(message)

    def check_task_status(self, sprint, status):
        if not sprint and status != Task.STATUS_TODO:
            self.show_error('Backlog tasks must have "Not Started" status')

    def check_started_date(self, started, status):
        if started and status == Task.STATUS_TODO:
            self.show_error('Started date cannot be set for not started tasks')

    def check_completed_date(self, completed, status):
        if completed and status != Task.STATUS_DONE:
            self.show_error(
                'Completed date cannot be set for uncompleted tasks')

    def show_error(self, message):
        message_error = ugettext_lazy(message)
        raise serializers.ValidationError(message_error)
