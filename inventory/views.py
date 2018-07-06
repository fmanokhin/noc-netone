from django.shortcuts import render

# Create your views here.
def pop_list(request):
    return render(request, 'inventory/pop_list.html', {})
