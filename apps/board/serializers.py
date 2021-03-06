from datetime import date
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint
from .models import Task
from .mixin import ValidatorMixin


User = get_user_model()


class SprintSerializer(ValidatorMixin, serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', 'links', )
    
    def get_links(self, obj):
        request = self.context['request']

        return {
            'self': reverse(
                'sprint-detail', 
                kwargs={'pk': obj.pk}, 
                request=request
            ),
            'tasks': reverse(
                'task-list',
                request=request
            ) + f'?sprint={obj.pk}',
        }

    def validate_end(self, value):
        new = self.instance is None
        changed = self.instance and self.instance.end != value

        if (new or changed) and (value < date.today()):
            self.show_error('End date cannot be in the past.')

        return value


class TaskSerializer(ValidatorMixin, serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, 
        required=False,
        allow_null=True, 
        queryset=User.objects.all()
    )
    status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'description',
            'sprint',
            'status',
            'status_display',
            'order',
            'assigned',
            'started',
            'due',
            'completed',
            'links',
        )

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse(
                'task-detail',
                kwargs={'pk': obj.pk},
                request=request
            ),
            'sprint': None,
            'assigned': None,
        }

        if obj.sprint_id:
            links['sprint'] = reverse(
                'sprint-detail',
                kwargs={'pk': obj.sprint_id},
                request=request
            )
            
        if obj.assigned:
            links['assigned'] = reverse(
                'user-detail', 
                kwargs={User.USERNAME_FIELD: obj.assigned}, 
                request=request,
            )

        return links

    def validate_sprint(self, value):
        if self.instance and self.instance.pk:
            self.check_value_sprint(value, Task)
        else:
            self.check_if_is_not_a_old_sprint(
                value, 'Cannot add tasks to past sprints')
        
        return value

    def validate(self, attrs):
        sprint = attrs.get('sprint')
        status = attrs.get('status', Task.STATUS_TODO)
        started = attrs.get('started')
        completed = attrs.get('completed')

        self.check_task_status(sprint, status, Task)
        self.check_started_date(started, status, Task)
        self.check_completed_date(completed, status, Task)

        return attrs


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        task_url = reverse('task-list', request=request)

        return {
            'self': reverse(
                'user-detail', 
                kwargs={User.USERNAME_FIELD: username}, 
                request=request
            ),
            'tasks': f'{task_url}?assigned={username}'
        }
