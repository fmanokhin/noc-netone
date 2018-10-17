from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import Pop, Core, Customer, Device, Network
from .forms import PopForm, CoreForm, CustomerForm, CustomerConnectionForm, DeviceForm, NetworkForm
from .filters import PopFilter, CoreFilter, CustomerFilter, DeviceFilter, NetworkFilter, NetworkFilterNoStut
import ipaddress, iptools

# Create your views here.
# Отобразить точки присутствия
@login_required
def pop_list(request):
    pops = Pop.objects.all()
    popfilter = PopFilter(request.POST, queryset=pops)
    context = {'pops': pops, 'filter': popfilter}
    return render(request, 'inventory/pop_list.html', context)

# Отображение данных по точке присутствия
@login_required
def pop_detail(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    device = Pop.objects.get(pk=pk).device_set.all()
    network = Pop.objects.get(pk=pk).network_set.all()
    upstream = Pop.objects.get(pk=pk).core_set.all()
    downstream = Pop.objects.get(pk=pk).customer_set.all()
    otherpopsdownstream = Pop.objects.get(pk=pk).otherpopsdownstream.all()
    otherpopsupstream = Pop.objects.get(pk=pk).otherpopsupstream.all()
    context = {'pop': pop, 'device': device, 'network': network, 'upstream': upstream, 'downstream': downstream, 'otherpopsdownstream': otherpopsdownstream, 'otherpopsupstream': otherpopsupstream}
    return render(request, 'inventory/pop_detail.html', context)

# Создать точку присутствия
@login_required
def pop_new(request):
    if request.method == "POST":
        form = PopForm(request.POST)
        if form.is_valid():
         pop = form.save(commit=False)
         pop.save()
        return redirect('pop_detail', pk=pop.pk)
    else:
        form = PopForm()
    return render(request, 'inventory/pop_edit.html', {'form': form})

# Редактировать точку присутствия
@login_required
def pop_edit(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    if request.method == "POST":
        form = PopForm(request.POST, instance=pop)
        if form.is_valid():
            pop = form.save(commit=False)
            pop.save()
            return redirect('pop_detail', pk=pop.pk)
    else:
        form = PopForm(instance=pop)
    return render(request, 'inventory/pop_edit.html', {'form': form})

#Удалить точку присутствия
@login_required
def pop_remove(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    try:
        pop.delete()
    except:
        return render(request, 'inventory/error_delete.html')
    return redirect('pop_list')

# Отобразить опорные узлы
@login_required
def core_list(request):
    cores = Core.objects.all()
    corefilter = CoreFilter(request.POST, queryset=cores)
    context = {'cores': cores, 'filter': corefilter}
    return render(request, 'inventory/core_list.html', context)

# Отображение данных по опорному узлу
@login_required
def core_detail(request, pk):
    core = get_object_or_404(Core, pk=pk)
    device = Core.objects.get(pk=pk).device_set.all()
    network = Core.objects.get(pk=pk).network_set.all()
    downstream = Core.objects.get(pk=pk).pop_set.all()
    context = {'core': core, 'device': device, 'network': network, 'downstream': downstream}
    return render(request, 'inventory/core_detail.html', context)

# Создать опорный узел
@login_required
def core_new(request):
    if request.method == "POST":
        form = CoreForm(request.POST)
        if form.is_valid():
         core = form.save(commit=False)
         core.save()
        return redirect('core_detail', pk=core.pk)
    else:
        form = CoreForm()
    return render(request, 'inventory/core_edit.html', {'form': form})

# Редактировать опорный узел
@login_required
def core_edit(request, pk):
    core = get_object_or_404(Core, pk=pk)
    if request.method == "POST":
        form = CoreForm(request.POST, instance=core)
        if form.is_valid():
            core = form.save(commit=False)
            core.save()
            return redirect('core_detail', pk=core.pk)
    else:
        form = CoreForm(instance=core)
    return render(request, 'inventory/core_edit.html', {'form': form})

#Удалить опорный узел присутствия
@login_required
def core_remove(request, pk):
    core = get_object_or_404(Core, pk=pk)
    try:
        core.delete()
    except:
        return render(request, 'inventory/error_delete.html')
    return redirect('core_list')

# Связки
# На Корах (оборудование)
@login_required
def core_devices(request, pk):
    core = get_object_or_404(Core, pk=pk)
    devices = Device.objects.all()
    device = Core.objects.get(pk=pk).device_set.all()
    devicesfilter = DeviceFilter(request.POST, queryset=devices)
    context = {'core': core, 'device': device, 'devices': devices, 'filter': devicesfilter}
    return render(request, 'inventory/core_devices.html', context)

@login_required
def core_device_remove(request, corepk, devicepk):
    Device.objects.get(pk=devicepk).core_set.remove(Core.objects.get(pk=corepk))
    Core.objects.get(pk=corepk).device_set.remove(Device.objects.get(pk=devicepk))
    return redirect('core_detail', corepk)

@login_required
def core_device_add(request, corepk, devicepk):
    Device.objects.get(pk=devicepk).core_set.add(Core.objects.get(pk=corepk))
    Core.objects.get(pk=corepk).device_set.add(Device.objects.get(pk=devicepk))
    return redirect('core_detail', corepk)

# На Корах (даунстримы)
@login_required
def core_downstreams(request, pk):
    core = get_object_or_404(Core, pk=pk)
    pops = Pop.objects.all()
    downstream = Core.objects.get(pk=pk).pop_set.all()
    popfilter = PopFilter(request.POST, queryset=pops)
    context = {'core': core, 'downstream': downstream, 'pops': pops, 'filter': popfilter}
    return render(request, 'inventory/core_downstreams.html', context)

@login_required
def core_downstreams_remove(request, corepk, poppk):
    Core.objects.get(pk=corepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.remove(Core.objects.get(pk=corepk))
    return redirect('core_detail', corepk)

@login_required
def core_downstreams_add(request, corepk, poppk):
    Core.objects.get(pk=corepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.add(Core.objects.get(pk=corepk))
    return redirect('core_detail', corepk)

# На Корах (IPv4)
@login_required
def core_ipv4networks(request, pk):
    core = get_object_or_404(Core, pk=pk)
    ipv4networks = Network.objects.all()
    ipv4networkfilter = NetworkFilterNoStut(request.POST, queryset=ipv4networks)
    core_ipv4 = Core.objects.get(pk=pk).network_set.all()
    context = {'core': core, 'ipv4networks': ipv4networks, 'core_ipv4': core_ipv4, 'filter': ipv4networkfilter}
    return render(request, 'inventory/core_ipv4.html', context)

@login_required
def core_ipv4network_remove(request, corepk, networkpk):
    Core.objects.get(pk=corepk).network_set.remove(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'FREE'
    network.save(update_fields=['status'])
    return redirect('core_detail', corepk)

@login_required
def core_ipv4network_add(request, corepk, networkpk):
    Core.objects.get(pk=corepk).network_set.add(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'BUSY'
    network.save(update_fields=['status'])
    return redirect('core_detail', corepk)

# На Точках присутствия (IPv4)
@login_required
def pop_ipv4networks(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    ipv4networks = Network.objects.all()
    ipv4networkfilter = NetworkFilterNoStut(request.POST, queryset=ipv4networks)
    pop_ipv4 = Pop.objects.get(pk=pk).network_set.all()
    context = {'pop': pop, 'ipv4networks': ipv4networks, 'pop_ipv4': pop_ipv4, 'filter': ipv4networkfilter}
    return render(request, 'inventory/pop_ipv4.html', context)

@login_required
def pop_ipv4network_remove(request, poppk, networkpk):
    Pop.objects.get(pk=poppk).network_set.remove(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'FREE'
    network.save(update_fields=['status'])
    return redirect('pop_detail', poppk)

@login_required
def pop_ipv4network_add(request, poppk, networkpk):
    Pop.objects.get(pk=poppk).network_set.add(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'BUSY'
    network.save(update_fields=['status'])
    return redirect('pop_detail', poppk)

# На Точках присутствия (оборудование)
@login_required
def pop_devices(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    devices = Device.objects.all()
    device = Pop.objects.get(pk=pk).device_set.all()
    devicesfilter = DeviceFilter(request.POST, queryset=devices)
    context = {'pop': pop, 'device': device, 'devices': devices, 'filter': devicesfilter}
    return render(request, 'inventory/pop_devices.html', context)

@login_required
def pop_device_remove(request, poppk, devicepk):
    Device.objects.get(pk=devicepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).device_set.remove(Device.objects.get(pk=devicepk))
    return redirect('pop_detail', poppk)

@login_required
def pop_device_add(request, poppk, devicepk):
    Device.objects.get(pk=devicepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).device_set.add(Device.objects.get(pk=devicepk))
    return redirect('pop_detail', poppk)


# На Точках присутствия (апстримы)
@login_required
def pop_upstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    cores = Core.objects.all()
    upstream = Pop.objects.get(pk=pk).core_set.all()
    corefilter = CoreFilter(request.POST, queryset=cores)
    context = {'pop': pop, 'upstream': upstream, 'cores': cores, 'filter': corefilter}
    return render(request, 'inventory/pop_upstreams.html', context)

@login_required
def pop_upstreams_remove(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.remove(Core.objects.get(pk=corepk))
    return redirect('pop_detail', poppk)

@login_required
def pop_upstreams_add(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.add(Core.objects.get(pk=corepk))
    return redirect('pop_detail', poppk)

# На Точках присутствия (апстрим- другие точки)
@login_required
def otherpop_upstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    otherpops = Pop.objects.all()
    otherpopsupstream = Pop.objects.get(pk=pk).otherpopsupstream.all()
    popfilter = PopFilter(request.POST, queryset=otherpops)
    context = {'pop': pop, 'otherpopsupstream': otherpopsupstream, 'otherpops': otherpops, 'filter': popfilter}
    return render(request, 'inventory/otherpops_upstreams.html', context)

@login_required
def otherpop_upstreams_remove(request, otherpoppk, poppk):
    Pop.objects.get(pk=otherpoppk).otherpops_upstream.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).otherpops_downstream.remove(Pop.objects.get(pk=otherpoppk))
    return redirect('pop_detail', poppk)

@login_required
def otherpop_upstreams_add(request, otherpoppk, poppk):
    Pop.objects.get(pk=otherpoppk).otherpops_upstream.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).otherpops_downstream.add(Pop.objects.get(pk=otherpoppk))
    return redirect('pop_detail', poppk)

# На Точках присутсвия (даунстримы-другие точки)
@login_required
def otherpop_downstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    otherpops = Pop.objects.all()
    otherpopsdownstream = Pop.objects.get(pk=pk).otherpopsdownstream.all()
    popfilter = PopFilter(request.POST, queryset=otherpops)
    context = {'pop': pop, 'otherpopsdownstream': otherpopsdownstream, 'otherpops': otherpops, 'filter': popfilter}
    return render(request, 'inventory/otherpops_downstreams.html', context)

@login_required
def otherpop_downstreams_remove(request, otherpoppk, poppk):
    Pop.objects.get(pk=otherpoppk).otherpops_downstream.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).otherpops_upstream.remove(Pop.objects.get(pk=otherpoppk))
    return redirect('pop_detail', poppk)

@login_required
def otherpop_downstreams_add(request, otherpoppk, poppk):
    Pop.objects.get(pk=otherpoppk).otherpops_downstream.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).otherpops_upstream.add(Pop.objects.get(pk=otherpoppk))
    return redirect('pop_detail', poppk)

# На Точках присутствия (даунстримы-клиенты)
@login_required
def pop_downstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    customers = Customer.objects.all()
    downstream = Pop.objects.get(pk=pk).customer_set.all()
    customerfilter = CustomerFilter(request.POST, queryset=customers)
    context = {'pop': pop, 'downstream': downstream, 'customers': customers, 'filter': customerfilter}
    return render(request, 'inventory/pop_downstreams.html', context)

@login_required
def pop_downstreams_remove(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.remove(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.remove(Pop.objects.get(pk=poppk))
    return redirect('pop_detail', poppk)

@login_required
def pop_downstreams_add(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.add(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.add(Pop.objects.get(pk=poppk))
    return redirect('pop_detail', poppk)

# На Клиентах (апстримы)
@login_required
def customer_upstreams(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    pops = Pop.objects.all()
    upstream = Customer.objects.get(pk=pk).pop_set.all()
    popfilter = PopFilter(request.POST, queryset=pops)
    context = {'customer': customer, 'upstream': upstream, 'pops': pops, 'filter': popfilter}
    return render(request, 'inventory/customer_upstreams.html', context)

@login_required
def customer_upstreams_remove(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.remove(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.remove(Pop.objects.get(pk=poppk))
    return redirect('customer_detail', customerpk)

@login_required
def customer_upstreams_add(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.add(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.add(Pop.objects.get(pk=poppk))
    return redirect('customer_detail', customerpk)

# На Клиентах (IPv4)
@login_required
def customer_ipv4networks(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    ipv4networks = Network.objects.all()
    ipv4networkfilter = NetworkFilterNoStut(request.POST, queryset=ipv4networks)
    customer_ipv4 = Customer.objects.get(pk=pk).network_set.all()
    context = {'customer': customer, 'ipv4networks': ipv4networks, 'customer_ipv4': customer_ipv4, 'filter': ipv4networkfilter}
    return render(request, 'inventory/customer_ipv4.html', context)

@login_required
def customer_ipv4network_remove(request, customerpk, networkpk):
    Customer.objects.get(pk=customerpk).network_set.remove(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'FREE'
    network.save(update_fields=['status'])
    return redirect('customer_detail', customerpk)

@login_required
def customer_ipv4network_add(request, customerpk, networkpk):
    Customer.objects.get(pk=customerpk).network_set.add(Network.objects.get(pk=networkpk))
    network = Network.objects.get(pk=networkpk)
    network.status = 'BUSY'
    network.save(update_fields=['status'])
    return redirect('customer_detail', customerpk)

# Клиенты
# Отобразить всех клиентов
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    customerfilter = CustomerFilter(request.POST, queryset=customers)
    context = {'customers': customers, 'filter': customerfilter}
    return render(request, 'inventory/customer_list.html', context)

# Отображение данных по клиенту
@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    upstream = Customer.objects.get(pk=pk).pop_set.all()
    network = Customer.objects.get(pk=pk).network_set.all()
    context = {'customer': customer, 'upstream': upstream, 'network': network}
    return render(request, 'inventory/customer_detail.html', context)

# Создать клиента
@login_required
def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
         customer = form.save(commit=False)
         customer.save()
        return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'inventory/customer_edit.html', {'form': form})

# Редактировать клиента
@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'inventory/customer_edit.html', {'form': form})

#Удалить клиента
@login_required
def customer_remove(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    try:
        customer.delete()
    except:
        return render(request, 'inventory/error_delete.html')
    return redirect('customer_list')

#Редактировать детали подключения клиента
@login_required
def customer_connection(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerConnectionForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerConnectionForm(instance=customer)
    return render(request, 'inventory/customer_connection.html', {'form': form})

# Оборудование
# Список всего оборудования
@login_required
def device_list(request):
    devices = Device.objects.all()
    devicesfilter = DeviceFilter(request.POST, queryset=devices)
    context = {'devices': devices, 'filter': devicesfilter}
    return render(request, 'inventory/device_list.html', context)

@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    context = {'device': device}
    return render(request, 'inventory/device_detail.html', context)

@login_required
def device_new(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
         device = form.save(commit=False)
         device.save()
        return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm()
    return render(request, 'inventory/device_edit.html', {'form': form})

# Редактировать устройство
@login_required
def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            device = form.save(commit=False)
            device.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'inventory/device_edit.html', {'form': form})

# Удалить устройство
@login_required
def device_remove(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('device_list')

#IPv4
@login_required
def ipv4_list(request):
    ipv4networks = Network.objects.all()
    ipv4networkfilter = NetworkFilter(request.POST, queryset=ipv4networks)
    context = {'ipv4networks': ipv4networks, 'filter': ipv4networkfilter}
    return render(request, 'inventory/ipv4_list.html', context)

@login_required
def ipv4_detail(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    mask = (ipaddress.ip_network(ipv4network.network)).netmask
    gwfind = list(iptools.IpRangeList(ipv4network.network).__iter__())
    gw = gwfind[1]
    ipfrom = gwfind[2]
    ipto = gwfind[-2]
    context = {'ipv4network': ipv4network, 'mask': mask, 'gw': gw, 'ipfrom': ipfrom, 'ipto': ipto}
    return render(request, 'inventory/ipv4_detail.html', context)

@login_required
def ipv4_new(request):
    if request.method == "POST":
        form = NetworkForm(request.POST)
        if form.is_valid():
            ipv4network = form.save(commit=False)
            if ipaddress.ip_network(ipv4network.network):
                ipv4network.save()
            else: form = NetworkForm()
        return redirect('ipv4_detail', pk=ipv4network.pk)
    else:
        form = NetworkForm()
    return render(request, 'inventory/ipv4_edit.html', {'form': form})

@login_required
def ipv4_edit(request, pk):
    ipv4network = get_object_or_404(Network, pk=pk)
    if request.method == "POST":
        form = NetworkForm(request.POST, instance=ipv4network)
        if form.is_valid():
            ipv4network = form.save(commit=False)
            ipv4network.save()
            return redirect('ipv4_detail', pk=ipv4network.pk)
    else:
        form = NetworkForm(instance=ipv4network)
    return render(request, 'inventory/ipv4_edit.html', {'form': form})

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

#Фильтрация
@login_required
def popfilter(request):
    poplist = Pop.objects.all()
    popfilter = PopFilter(request.POST, queryset=poplist)
    return render(request, 'inventory/pop_filter.html', {'filter': popfilter})
