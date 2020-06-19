from django import forms
from userApp.models import Customer, Person


class CustomerAdminForm(form.ModelForm):
    class Meta:
        model = Customer
        exclude = ('created_date', 'modified_date')

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('created_date', 'modified_date')