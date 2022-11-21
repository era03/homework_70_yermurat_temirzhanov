from tokenize import group
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.models import Projects, Tasks
from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm, TaskForm, AddUserToProjectForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class GroupPermissions(UserPassesTestMixin):

    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Projects
    context_object_name = 'projects'
    ordering = ('created_at',)


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Projects
    context_object_name = 'project'

    
class ProjectCreateView(GroupPermissions, LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Projects
    groups = ['Project Manager']

    def get_success_url(self):
        return reverse('projects')


class ProjectTaskCreateView(GroupPermissions, LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'task_create.html'
    groups = ['Project Manager', 'Developer']

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects')


class ProjectDeleteView(GroupPermissions, LoginRequiredMixin, DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Projects
    success_url = reverse_lazy('index')
    groups = ['Project Manager']


class AddUserToProjectView(GroupPermissions, LoginRequiredMixin, UpdateView):
    model = Projects
    form_class = AddUserToProjectForm
    template_name = 'add_user_to_project.html'
    context_object_name = 'project'
    groups = ['Project Manager', 'Team Lead']

    def get_success_url(self):
        return reverse('projects')