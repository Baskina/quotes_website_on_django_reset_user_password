from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm, CharField, TextInput, ModelChoiceField

from authorsapp.models import Author
from quotesapp.models import Quote, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())
    tags = ArrayField(ModelChoiceField(queryset=Tag.objects.all()))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

