from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos')
