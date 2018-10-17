from django import forms

from .models import Pop, Core, Customer, Device, Network

class PopForm(forms.ModelForm):

    class Meta:
        model = Pop
        fields = ('title','address', 'contacts', 'manager', 'bandwidth', 'vlans', 'comments',)

class CoreForm(forms.ModelForm):

    class Meta:
        model = Core
        fields = ('title','address', 'contacts','manager', 'bandwidth', 'vlans','comments',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('title','address', 'contacts', 'manager', 'comments',)

class CustomerConnectionForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('switch','vlans', 'bandwidth',)

class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('vendor', 'model', 'dnsname', 'ipaddress', 'geoaddress', 'comments', 'serialnum')

class NetworkForm(forms.ModelForm):

    class Meta:
        model = Network
        fields = ('network', 'status', 'segment', 'comment',)
