from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    text = forms.CharField(max_length=50,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Add a todo',
            }))

    class Meta:
        model = Todo
        fields = {'text'}