from django.shortcuts import render
from .models import Pop

# Create your views here.
def pop_list(request):
    pops = Pop.objects.all()
    return render(request, 'inventory/pop_list.html', {'pops': pops})
