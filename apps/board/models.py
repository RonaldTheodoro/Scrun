from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy


class Sprint(models.Model):
    name = models.CharField('name', max_length=100, blank=True, default='')
    description = models.TextField('description', blank=True, default='')
    end = models.DateField('end', unique=True)

    def __str__(self):
        return self.name or ugettext_lazy(f'Sprint ending {self.end}')
        

class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, ugettext_lazy('Not Started')),
        (STATUS_IN_PROGRESS, ugettext_lazy('In Progress')),
        (STATUS_TESTING, ugettext_lazy('Testing')),
        (STATUS_DONE, ugettext_lazy('Done')),
    )

    name = models.CharField('name', max_length=100)
    description = models.TextField('description', blank=True, default='')
    sprint = models.ForeignKey(
        'Sprint', verbose_name='Sprint', blank=True, null=True)
    status = models.SmallIntegerField(
        'status', choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField('order', default=0)
    assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='assigned', 
        null=True, 
        blank=True
    )
    started = models.DateField('started', blank=True, null=True)
    due = models.DateField('due', blank=True, null=True)
    completed = models.DateField('completed', blank=True, null=True)

    def __str__(self):
        return self.name