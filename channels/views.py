from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import L2VPN
from .forms import L2VPNForm
from django.db.models import Q

from inventory.models import Customer
from inventory.filters import CustomerFilter

# Create your views here.
#Cписок всех L2VPN
@login_required
def l2vpn_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        l2vpns = L2VPN.objects.filter(
        Q(channelid__icontains=search_query) |
        Q(customer__title__icontains=search_query) |
        Q(coreA__title__icontains=search_query) |
        Q(coreB__title__icontains=search_query) |
        Q(pointA__title__icontains=search_query) |
        Q(pointB__title__icontains=search_query) |
        Q(vlan__icontains=search_query)
        )
    else:
        l2vpns = L2VPN.objects.all()
    context = {'l2vpns': l2vpns}
    return render(request, 'channels/l2vpn_list.html', context)

#Отображение данных по каналу L2VPN
@login_required
def l2vpn_detail(request, pk):
    l2vpn = get_object_or_404(L2VPN, pk=pk)
    context = {'l2vpn': l2vpn}
    return render(request, 'channels/l2vpn_detail.html', context)

#Создать новый канал L2VPN
@login_required
def l2vpn_new(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        form = L2VPNForm(request.POST)
        if form.is_valid():
            l2vpn = form.save(commit=False)
            l2vpn.save()
            return redirect('l2vpn_detail', pk=l2vpn.pk)
    else:
        form = L2VPNForm()
    context = {'form': form, 'customers': customers}
    return render(request, 'channels/l2vpn_edit.html', context)

#Редактировать канал L2VPN
@login_required
def l2vpn_edit(request, pk):
    l2vpn = get_object_or_404(L2VPN, pk=pk)
    if request.method == "POST":
        form = L2VPNForm(request.POST, instance=l2vpn)
        if form.is_valid():
            l2vpn = form.save(commit=False)
            l2vpn.save()
            return redirect('l2vpn_detail', pk=l2vpn.pk)
    else:
        form = L2VPNForm(instance=l2vpn)
    return render(request, 'channels/l2vpn_edit.html', {'form': form})

#Удалить канал L2VPN
@login_required
def l2vpn_remove(request, pk):
    l2vpn = get_object_or_404(L2VPN, pk=pk)
    l2vpn.delete()
    return redirect('l2vpn_list')
