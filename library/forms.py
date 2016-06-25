from django import forms
from library.models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'pubyr', 'type', 'cost', 'comments']
        widgets = {'type':forms.RadioSelect(),
                'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
                'cost':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
                'pubyr':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Publish year'}),
                'comments':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comments'}),
                }
        labels = {'cost':'Estimated Cost in Dollars'}

class SearchlibForm(forms.Form):
    title = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}))
    author = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Author'}))
