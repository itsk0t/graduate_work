from django import forms

from comments.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'text'
        ]

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Введите текст'}),
        }
