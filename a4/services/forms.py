from django import forms
from .models import OrderRequest

class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['service', 'sub_service', 'description']
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-control',
                'id': 'service',
                'required': True,
            }),
            'sub_service': forms.Select(attrs={
                'class': 'form-control',
                'id': 'sub_service',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш заказ',
                'required': True,
            }),
        }