from django import forms
from library.models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = []

class SearchlibForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
