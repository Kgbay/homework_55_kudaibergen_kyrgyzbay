from django import forms
from django.core.exceptions import ValidationError


STATUS_CHOICES = (
    ("Active", "Активно"),
    ("Not active", "Не активно")
)

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    status = forms.ChoiceField(required=True, label='Статус', choices=STATUS_CHOICES)
    custom_date = forms.DateField(required=True, label='Дата')
    author = forms.CharField(max_length=50, required=True, label='Автор')
    full_desc = forms.CharField(max_length=1000, required=True, label='Описание')

    title.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Загаловок'})
    status.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Статус'})
    custom_date.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Дата'})
    author.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Автор'})
    full_desc.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Описание'})


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError("Загаловок должен быть длиннее 2 символов")
        return title