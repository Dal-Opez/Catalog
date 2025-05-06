from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from config.settings import SPAM


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at',]
        # fields = ['name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at']



    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name.lower())
        for word in SPAM:
            if word in name.lower():
                raise ValidationError('Описание содержит запрещенные слова')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in SPAM:
            if word in description.lower():
                raise ValidationError('Описание содержит запрещенные слова')
        return description