from rest_framework import serializers
from webapp.models import Tasks, Projects



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id', 'task', 'description', 'project', 'status', 'type', 'created_at', 'updated_at', 'is_deleted')
        read_only_fields = ('project', 'status', 'type')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'project', 'description', 'created_at', 'deadline', 'users')
        read_only_fields = ('user', )