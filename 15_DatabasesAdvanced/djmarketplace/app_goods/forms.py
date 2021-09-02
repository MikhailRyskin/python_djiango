from django import forms


class PeriodForm(forms.Form):
    date_from = forms.DateField(help_text='дата начала периода')
    date_to = forms.DateField(help_text='дата конца периода')
