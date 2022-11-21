from django.urls import path
from api.views import TaskDetailView, ProjectDetailView



urlpatterns = [
    path('task/<int:pk>/', TaskDetailView.as_view()),
    path('project/<int:pk>/', ProjectDetailView.as_view())
]