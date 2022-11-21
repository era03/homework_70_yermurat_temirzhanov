from django.forms import ValidationError
from webapp.models import Tasks, Projects
from django import forms


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError('The max number of characters is 20')
    return string


def min_length_validator(string):
    if len(string) < 8:
        raise ValidationError('The minimum number of characters is 8')
    return


class TaskForm(forms.ModelForm):

    task = forms.CharField(validators=(min_length_validator, max_length_validator))

    class Meta:
        model = Tasks
        fields = ('task', 'description', 'type', 'status')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')


class ProjectForm(forms.ModelForm):

    project = forms.CharField(validators=(min_length_validator, max_length_validator))

    class Meta:
        model = Projects
        fields = ('project', 'created_at', 'deadline')


class AddUserToProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('users', )
    