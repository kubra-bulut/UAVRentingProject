from django import forms
from .models import RentedUavs


# creating a form
class UavForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs=
    {
        'class': 'datepicker'
    }))

    
    # create meta class
    class Meta:
        # specify model to be used
        model = RentedUavs

        fields = ['id',  'uav', 'date', 'member']

        #fields = '__all__'

       

       


       

        