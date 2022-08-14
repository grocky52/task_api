from rest_framework import serializers, reverse
from .models import Sprint, Task
from django.contrib.auth import get_user_model
User = get_user_model()

class Sprinterserializers(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', 'links')

    def get_links(self, obj): #returns a nested dictianary containning all thelinks that should be incliided in an api schema
        request = self.context['request']
        return{
            'self':reverse('sprint-details', kwargs={'pk':obj.pk}, request=request)
        }



class Taskserializer(serializers.ModelSerializer):
    assigned = serializers.SlugRelatedField(
        slug_field= User.USERNAME_FIELD, required=False, allow_null=True,
        queryset = User.objects.all()
    )
    status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint', 'status', 'status_dissplay', 'order', 'assigned', 'started', 'due', 'complete', 'links')

    def get_status_display(self, obj): #gets human redable version of the status 
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self':reverse('task-details', kwargs = {'pk':obj.pk}, request=request)
        }
        if obj.sprint_id:
            links['sprint'] = reverse('sprint-details', kwargs={'pk':obj.sprint_id}, request=request)
        if obj.assigned:
            links['assigned'] = reverse('user-details', kwargs={User.USERNAME_FIELD: objj.assigned}, request=request)

class Userserializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields =( 'id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')

    def get_links(self, obj):
        request = self.context['request '] #request is used to ask data inside a seriializer 
        username = obj.get_username()
        return{
            'self':reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
            'sprint':None,
            'assigned':None,

        }

        