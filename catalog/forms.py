from django import forms

from users.forms import StyleFromMixin
from .models import Product
from django.core.exceptions import ValidationError
from config.settings import SPAM


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at', 'is_published']
        # fields = ['name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость товара'
        })

        self.fields['owner'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите владельца товара'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name.lower())
        for word in SPAM:
            if word in name.lower():
                raise ValidationError('Наименование содержит запрещенные слова!')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in SPAM:
            if word in description.lower():
                raise ValidationError('Описание содержит запрещенные слова!')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Задана отрицательная стоимость товара!')
        return price

class ProductModeratorForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published', ]

