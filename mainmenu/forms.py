from django import forms
from mainmenu.models import coustmers


class coustmer_form(forms.ModelForm):
    class Meta:
        model=coustmers

        fields=['name','age','designation','time']

        widgets={
            'name':forms.TextInput(attrs={'class':'forms-control','placeholder':'enter coustmer name'}),
            'age':forms.TextInput(attrs={'class':'forms-control','placeholder':'enter coustmer age'}),
            'designation':forms.TextInput(attrs={'class':'forms-control','placeholder':'enter coustmer designation'}),
            'time':forms.TimeInput(attrs={'class':'forms-control','placeholder':'enter coustmer entered time'})
        }


        

