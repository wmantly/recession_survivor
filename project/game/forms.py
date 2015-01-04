from django import forms
from game.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from pprint import pprint as print
from django.core.exceptions import ValidationError
import datetime

def val_round(val_round):
    if (val_round<=0):
        raise ValidationError("Round must be greater 0", code='invalid')

def val_bal(bal):
    if(bal<=0):
        raise ValidationError("Balance must be greater than 0",code='invalid')

def val_date(date):

    print('val_date')
    d = datetime.datetime.now()
    dated = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    if (dated >= d.date()):
        raise ValidationError("This date must be in the past", code='invalid')

class DateInput(forms.DateInput):
    input_type = 'date'

class GameCreateForm( ModelForm ):
    balance = forms.DecimalField(validators=[val_bal], initial=10000)
    total_rounds = forms.IntegerField(initial=12)
    current_date = forms.CharField( widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Whole_Game
        fields = ( 'name', 'balance', 'total_rounds' , 'game_type', 'current_date' )
        labels = {
            'current_date': _('Starting Day of Your Game (use format 9/20/2011)')
        }


    def clean(self):
        # print(dir(self))
        data = self.cleaned_data
        val_round(data['total_rounds'])
        val_date(data['current_date'])
        print(data)
        if 'name' or 'balance' or 'total_rounds' or 'game_type' or 'current_date' not in data:
            raise forms.ValidationError('PLease enter Valid Values ')
       
        cur_date = datetime.datetime.strptime( data['current_date'], "%Y-%m-%d" ).date()
        
        total_round = data['total_rounds']
        game_type = data['game_type']
        if game_type == 'weekly':
            num_days = 7 * total_round
        elif game_type == 'monthly':
            num_days = 31 * total_round
        elif game_type == 'yearly':
            num_days = 365 * total_round

        check_date = datetime.datetime.now().date() - datetime.timedelta(days=num_days)

        if(check_date <= cur_date):
            raise forms.ValidationError('Date must be further in the past')

    #     return self.cleaned_data


