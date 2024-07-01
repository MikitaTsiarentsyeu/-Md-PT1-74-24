from django import forms
from .models import Clients, Questions, Answers
# from nastya.views import poll

class AddClientModelForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = "name", "email", "telegram_account", "coments"


class Poll_Form(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    telegram_account = forms.CharField(max_length=50)


class Poll_Form_answ(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(), max_length=500)

