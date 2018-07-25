from datetimewidget.widgets import DateTimeWidget
from django import forms
from django.forms import DateField, TimeField

from .models import Hospital, Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class HospitalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['name'].label = 'Name'
        self.fields['address'].label = 'Address'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-text'
        })

        self.fields['address'].widget.attrs.update({
            'class': 'uk-text'
        })

    class Meta:
        model = Hospital
        fields = {'name', 'address'}


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['doctor'].label = 'Doctor'
        if kwargs:
            self.fields['doctor'].initial = kwargs.pop('doctor')
            self.fields['doctor'].queryset = kwargs.pop('doctors')
        self.fields['start_date'].label = 'Start time'
        self.fields['end_date'].label = 'End time'
        self.fields['patients_remarks'].label = 'Remarks'

        self.fields['doctor'].widget.attrs.update({
            'class': 'uk-width-auto uk-select'
        })
        self.fields['start_date'].widget.attrs.update({
            'class': 'uk-width-auto'
        })
        self.fields['end_date'].widget.attrs.update({
            'class': 'uk-width-auto'
        })
        self.fields['patients_remarks'].widget.attrs.update({
            'class': 'uk-width-auto uk-input'
        })

    def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        doctor = cleaned_data.get('doctor')
        start_time = cleaned_data.get('start_date')
        end_time = cleaned_data.get('end_date')
        if not doctor:
            raise forms.ValidationError("Doctor is a required field.")
        if start_time and end_time:
            if start_time > end_time:
                msg = u"Start time must be before the end time"
                self._errors['start_time'] = self.error_class([msg])
        elif not start_time:
            msg = u"Appointment start time is a required field"
            self._errors['start_time'] = self.error_class([msg])
        elif not end_time:
            msg = u"Appointment time is a required field"
            self._errors['end_time'] = self.error_class([msg])
        return cleaned_data

    def save(self, **kwargs):
        instance = super(AppointmentForm, self).save(commit=False)
        instance.save()
        return instance

    class Meta:
        model = Appointment
        fields = {'doctor', 'patients_remarks', 'start_date', 'end_date'}
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian': True
        }
        widgets = {
            'start_date': DateTimeWidget(options=dateTimeOptions),
            'end_date': DateTimeWidget(options=dateTimeOptions),
        }
