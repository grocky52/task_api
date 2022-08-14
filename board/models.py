from django.db import models
from django.conf  import settings

from django.utils.translation import gettext_lazy as _ #used to translate when the valiable is uccessed other than called as in ugettext prefixed u  means unicode 


class Sprint(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(blank=True, default='')
    end = models.DateTimeField(default='', blank=True)


    def __str__(self):
        return self.name or _('sprint ending %s') % self.end

class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO , _('Not started')),
        (STATUS_IN_PROGRESS , _('In progress')),
        (STATUS_TESTING , _('Testing')),
        (STATUS_DONE , _('Done')),

    )

    name = models.CharField(max_length=100)
    deescription = models.TextField(default='', blank = True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    started = models.DateTimeField(blank=True, null=True)
    due = models.DateTimeField(null=True, blank=True)
    complete = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
