from django import forms
from library.models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = []
