from django import forms

from .models import TodoList

class TodoForm(forms.ModelForm):
    completed = forms.BooleanField(label='Mark as complete')

    class Meta:
        model = TodoList
        fields = ('text',)