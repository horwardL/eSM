from django import forms
from catalogueApp.models import Category, Market, Product


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('created_date', 'modified_date')


class MarketAdminForm(forms.ModelForm):
    class Meta:
        model = Market
        exclude = ('created_date', 'modified_date')


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_date', 'modified_date')

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']