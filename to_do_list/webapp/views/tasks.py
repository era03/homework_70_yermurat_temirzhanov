from django.shortcuts import get_object_or_404, redirect
from webapp.forms import TaskForm
from webapp.models import Tasks
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin



class GroupPermissions:

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class TaskDetailView(DetailView):
    template_name = 'task_detail.html'
    model = Tasks
    context_object_name = 'task'


class TaskCreateView(GroupPermissions, LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    model = Tasks
    groups = ['Project Manager', 'Team Lead', 'Developer']

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(GroupPermissions, LoginRequiredMixin, UpdateView):
    template_name = 'task_edit.html'
    form_class = TaskForm
    model = Tasks
    context_object_name = 'task'
    groups = ['Project Manager', 'Team Lead', 'Developer']

    def get_success_url(self):
        return reverse('index')


class TaskDeleteView(GroupPermissions, LoginRequiredMixin, DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Tasks
    success_url = reverse_lazy('index')
    context_object_name = 'task'
    groups = ['Project Manager', 'Team Lead']
