from django.forms import ModelForm
from .models import booking
class bookingForm(ModelForm):
    class Meta:
        model = booking
        fields = '__all__'