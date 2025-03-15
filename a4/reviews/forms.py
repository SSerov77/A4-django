from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']  # Добавляем поле author
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'review_input',
                'placeholder': 'Напишите отзыв',
                'required': True,
            }),
            'author': forms.HiddenInput(),  # Скрываем поле author
        }