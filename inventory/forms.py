from django import forms

from .models import Pop

class PopForm(forms.ModelForm):

    class Meta:
        model = Pop
        fields = ('title','address', 'contacts', 'manager', 'bandwidth', 'vlans', 'comments',)
