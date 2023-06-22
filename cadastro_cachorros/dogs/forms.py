from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'weight', 'breed')

    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
