import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm, TextInput, ValidationError

from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        # Validating form fields using widgets
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'finish_date': DateInput(attrs={'type': 'date'}),
            'parking_space_number': TextInput(attrs={'pattern': '[1-9]+', 'title': 'Enter a valid parking space number'}),
            'phone_number': TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter digits only '}),
            'name': TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter characters only '}),
            'surname': TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter characters only '})
        }


    # def get_initial(self):
    #     print(self.request)
    #     self.initial.update({'name':self.request.first_name,
    #                         'surname': self.request.last_name})
    #     return super(ReservationForm,self).get_initial()
# Additional custom validator for start_date / finish_date fields
    def clean(self):
        print(self.cleaned_data.keys())
        data = self.cleaned_data
        start_date = data['start_date']
        finish_date = data['finish_date']

        if start_date > finish_date:
            raise ValidationError('Wrong start and finish dates.')

        if start_date < datetime.date.today():
            raise ValidationError('Start date in the past.')

        return data


class ParkingSpaceForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['parking_space_number']
        widgets = {
            'parking_space_number': TextInput(attrs={'pattern': '[1-9]+', 'title': 'Enter a valid parking space number'})
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
