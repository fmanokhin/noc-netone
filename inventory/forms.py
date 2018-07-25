from django import forms

from .models import Pop, Core

class PopForm(forms.ModelForm):

    class Meta:
        model = Pop
        fields = ('title','address', 'contacts', 'manager', 'bandwidth', 'vlans', 'comments',)

class CoreForm(forms.ModelForm):

    class Meta:
        model = Core
        fields = ('title','address', 'contacts',)
