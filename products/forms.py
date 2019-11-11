from django import forms

PRODUCT_TYPE_CHOICES = [
    ('energy', 'Energy'),
    ('relaxation', 'Relaxation'),
    ('combination', 'Combination'),
]

PRODUCT_SIZE_CHOICES = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
]

PRODUCT_FREQ_CHOICES = [
    ('weekly', 'Weekly'),
    ('biweekly', 'Bi-weekly'),
    ('monthly', 'Monthly'),
]

class SelectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product_type'].widget.attrs.update({
            'class': 'list-unstyled',
        })
        self.fields['product_size'].widget.attrs.update({
            'class': 'list-unstyled',
        })
        self.fields['product_freq'].widget.attrs.update({
            'class': 'list-unstyled',
        })

    product_type = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        choices=PRODUCT_TYPE_CHOICES,
    )

    product_size = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        choices=PRODUCT_SIZE_CHOICES,
    )

    product_freq = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(),
        choices=PRODUCT_FREQ_CHOICES,
    )
