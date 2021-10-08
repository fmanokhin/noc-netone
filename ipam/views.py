from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import Network
from .forms import NetworkForm

import ipaddress, iptools

from inventory.filters import NetworkFilter, NetworkFilterNoStut
# Create your views here.

#IPv4
@login_required
def ipv4_list(request):
    ipv4networks = Network.objects.all()
    ipv4networkfilter = NetworkFilter(request.POST, queryset=ipv4networks)
    context = {'ipv4networks': ipv4networks, 'filter': ipv4networkfilter}
    return render(request, 'ipam/ipv4_list.html', context)

@login_required
def ipv4_detail(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    mask = (ipaddress.ip_network(ipv4network.network)).netmask
    gwfind = list(iptools.IpRangeList(ipv4network.network).__iter__())
    gw = gwfind[1]
    ipfrom = gwfind[2]
    ipto = gwfind[-2]
    context = {'ipv4network': ipv4network, 'mask': mask, 'gw': gw, 'ipfrom': ipfrom, 'ipto': ipto}
    return render(request, 'ipam/ipv4_detail.html', context)

@login_required
def ipv4_new(request):
    if request.method == "POST":
        form = NetworkForm(request.POST)
        if form.is_valid():
            ipv4network = form.save(commit=False)
            try:
                if ipaddress.ip_network(ipv4network.network):
                    ipv4network.save()
                else:
                    pass
            except:
                 return render(request, 'inventory/error_subnet.html')
        return redirect('ipv4_detail', pk=ipv4network.pk)
    else:
        form = NetworkForm()
    return render(request, 'ipam/ipv4_edit.html', {'form': form})

@login_required
def ipv4_edit(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    if request.method == "POST":
        form = NetworkForm(request.POST, instance=ipv4network)
        if form.is_valid():
            ipv4network = form.save(commit=False)
            try:
                if ipaddress.ip_network(ipv4network.network):
                    ipv4network.save()
                else:
                    pass
            except:
                return render(request, 'inventory/error_subnet.html')
        return redirect('ipv4_detail', pk=ipv4network.pk)
    else:
        form = NetworkForm(instance=ipv4network)
    return render(request, 'ipam/ipv4_edit.html', {'form': form})

@login_required
def ipv4_sepor(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    subnets = list(ipaddress.ip_network(ipv4network).subnets())
    for subnet in subnets:
        Network.objects.create(network=subnet, segment=ipv4network.segment)
    ipv4network.delete()
    ipv4networks = Network.objects.all()
    return redirect('ipv4_list')

#Удалить подсеть
@login_required
def ipv4_remove(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    ipv4network.delete()
    return redirect('ipv4_list')
