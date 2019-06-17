from django import forms
from guest.models import Guest
from django.utils import timezone

class GuestForm(forms.ModelForm):
    
    class Meta:
        model = Guest
        fields = ("descriptin","image")

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.Textarea()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contatct-form'}))
    phone = forms.IntegerField(max_value=9999999999,min_value=1000000000)
    image = forms.ImageField(label = 'Choose your image',  help_text = 'The image should be cool.',required = False)
    date  = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datepicker'}),
        input_formats=('%Y-%m-%d %H:%M:%S', ),required = False)
    


     
