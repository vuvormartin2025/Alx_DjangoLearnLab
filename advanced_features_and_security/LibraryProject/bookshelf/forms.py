# bookshelf/forms.py
from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        label="Search",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search by title or author'})
    )

    def clean_q(self):
        q = self.cleaned_data.get('q', '').strip()
        # Extra sanitation example (remove dangerous characters if desired)
        # But avoid blind blacklists; prefer validation + ORM parameterization
        return q