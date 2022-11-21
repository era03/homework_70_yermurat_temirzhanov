from django.contrib import admin
from django.urls import path
from webapp.views.projects import ProjectsView, ProjectDetailView, ProjectCreateView, ProjectTaskCreateView, AddUserToProjectView
from webapp.views.base import IndexView
from webapp.views.tasks import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView




urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view()),
    path('tasks/<int:pk>/edit', TaskUpdateView.as_view(), name='edit_task'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<int:pk>/confirm-delete/', TaskDeleteView.as_view(), name='confirm_delete'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='detail_task'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/task/create', ProjectTaskCreateView.as_view(), name='create_task'),
    path('project/<int:pk>/add/user', AddUserToProjectView.as_view(), name='add_user_to_project')
]