from django.forms import ModelForm, CharField, TextInput, DateField
from authorsapp.models import Author


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(required=True, input_formats=['%Y-%m-%d'])
    description = CharField(min_length=3, max_length=1000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_location', 'born_date', 'description']
