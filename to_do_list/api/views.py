from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.models import Tasks, Projects
from api.serializers import TaskSerializer, ProjectSerializer
from rest_framework import status



class TaskDetailView(APIView):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs.get('pk'))
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs.get('pk'))
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs.get('pk'))
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Projects, pk=kwargs.get('pk'))
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        project = get_object_or_404(Projects, pk=kwargs.get('pk'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        project = get_object_or_404(Projects, pk=kwargs.get('pk'))
        serializer = TaskSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)