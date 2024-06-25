from django.forms import ModelForm
from django import forms
from .models import booking,UserComments
class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = '__all__'
           