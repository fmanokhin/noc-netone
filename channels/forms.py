from django import forms
from django.forms import SelectDateWidget, Select, NumberInput
from .models import L2VPN



class L2VPNForm(forms.ModelForm):

    class Meta:
        model = L2VPN
        fields = ('channelid','customer', 'coreA', 'coreB', 'pointA', 'pointB', 'deviceA', 'deviceB', 'portA', 'portB', 'vlan', 'speed', 'comments', 'on_date', 'off_date',)
        widgets = {
            'customer': Select(attrs={'class': 'js-example-basic-single'}),
            'coreA': Select(attrs={'class': 'js-example-basic-single'}),
            'coreB': Select(attrs={'class': 'js-example-basic-single'}),
            'pointA': Select(attrs={'class': 'js-example-basic-single'}),
            'pointB': Select(attrs={'class': 'js-example-basic-single'}),
            'deviceA': Select(attrs={'class': 'js-example-basic-single'}),
            'deviceB': Select(attrs={'class': 'js-example-basic-single'}),
            'on_date': SelectDateWidget(years=range(2006, 2031)),
            'off_date': SelectDateWidget(years=range(2006, 2031))
        }
