from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }
        labels = {
            "pat_name" : "Enter Patient's Name",
            "pat_email" : "Enter Patient's Email ID",
            "pat_phone" : "Enter PAtient's Phone Number",
            "doc_name" : "Choose Which Doctor do wanna See",
            "booking_date" : "Select date for the Apointment"
                }
