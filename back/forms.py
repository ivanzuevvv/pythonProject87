from django import forms


class PredictionForm(forms.Form):
    type_refuses = forms.CharField(label='Тип отказа (АО, НПО)', max_length=500)
    type_gpa = forms.CharField(label='Тип Гпа', max_length=500)
    type_say = forms.CharField(label='Тип Сау', max_length=500)
    type_equioment = forms.CharField(label='Внешнее проявление отказа', max_length=500, widget=forms.TextInput(attrs={'style': 'width: 100% !important;'}))
    refuses_element = forms.CharField(label='Отказавший элемент', max_length=500)





