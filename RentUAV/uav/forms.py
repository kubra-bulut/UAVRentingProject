from django import forms
from .models import Properties


# creating a form
class UavForm(forms.ModelForm):
    edob = forms.DateField(widget=forms.TextInput(attrs=
    {
        'class': 'datepicker'
    }))

    
    # create meta class
    class Meta:
        # specify model to be used
        model = Properties

        fields = ['id', 'brand', 'model', 'weight', 'category']

        #fields = '__all__'

       

       


       

        