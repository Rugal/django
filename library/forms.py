from django import forms
from library.models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'pubyr', 'type', 'cost', 'comments']
        widgets = {'type':forms.RadioSelect()}
        labels = {'cost':'Estimated Cost in Dollars'}

class SearchlibForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)

