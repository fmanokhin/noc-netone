from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from .models import Pop, Core, Customer, Device
from .forms import PopForm, CoreForm, CustomerForm, CustomerConnectionForm, DeviceForm

# Create your views here.
# Отобразить точки присутствия
def pop_list(request):
    pops = Pop.objects.all()
    return render(request, 'inventory/pop_list.html', {'pops': pops})

# Отображение данных по точке присутствия
def pop_detail(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    device = Pop.objects.get(pk=pk).device_set.all()
    upstream = Pop.objects.get(pk=pk).core_set.all()
    downstream = Pop.objects.get(pk=pk).customer_set.all()
    context = {'pop': pop, 'device': device, 'upstream': upstream, 'downstream': downstream}
    return render(request, 'inventory/pop_detail.html', context)

# Создать точку присутствия
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
def pop_remove(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    pop.delete()
    return redirect('pop_list')

# Отобразить опорные узлы
def core_list(request):
    cores = Core.objects.all()
    return render(request, 'inventory/core_list.html', {'cores': cores})

# Отображение данных по опорному узлу
def core_detail(request, pk):
    core = get_object_or_404(Core, pk=pk)
    device = Core.objects.get(pk=pk).device_set.all()
    downstream = Core.objects.get(pk=pk).pop_set.all()
    context = {'core': core, 'device': device, 'downstream': downstream}
    return render(request, 'inventory/core_detail.html', context)

# Создать опорный узел
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
def core_remove(request, pk):
    core = get_object_or_404(Core, pk=pk)
    core.delete()
    return redirect('core_list')

# Связки
# На Корах (оборудование)
def core_devices(request, pk):
    core = get_object_or_404(Core, pk=pk)
    devices = Device.objects.all()
    device = Core.objects.get(pk=pk).device_set.all()
    context = {'core': core, 'device': device, 'devices': devices}
    return render(request, 'inventory/core_devices.html', context)

def core_device_remove(request, corepk, devicepk):
    Device.objects.get(pk=devicepk).core_set.remove(Core.objects.get(pk=corepk))
    Core.objects.get(pk=corepk).device_set.remove(Device.objects.get(pk=devicepk))
    return redirect('core_detail', corepk)

def core_device_add(request, corepk, devicepk):
    Device.objects.get(pk=devicepk).core_set.add(Core.objects.get(pk=corepk))
    Core.objects.get(pk=corepk).device_set.add(Device.objects.get(pk=devicepk))
    return redirect('core_detail', corepk)

# На Корах (даунстримы)
def core_downstreams(request, pk):
    core = get_object_or_404(Core, pk=pk)
    pops = Pop.objects.all()
    downstream = Core.objects.get(pk=pk).pop_set.all()
    context = {'core': core, 'downstream': downstream, 'pops': pops}
    return render(request, 'inventory/core_downstreams.html', context)

def core_downstreams_remove(request, corepk, poppk):
    Core.objects.get(pk=corepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.remove(Core.objects.get(pk=corepk))
    return redirect('core_list')

def core_downstreams_add(request, corepk, poppk):
    Core.objects.get(pk=corepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.add(Core.objects.get(pk=corepk))
    return redirect('core_list')

# На Точках присутствия (оборудование)
def pop_devices(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    devices = Device.objects.all()
    device = Pop.objects.get(pk=pk).device_set.all()
    context = {'pop': pop, 'device': device, 'devices': devices}
    return render(request, 'inventory/pop_devices.html', context)

def pop_device_remove(request, poppk, devicepk):
    Device.objects.get(pk=devicepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).device_set.remove(Device.objects.get(pk=devicepk))
    return redirect('pop_detail', poppk)

def pop_device_add(request, poppk, devicepk):
    Device.objects.get(pk=devicepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).device_set.add(Device.objects.get(pk=devicepk))
    return redirect('pop_detail', poppk)


# На Точках присутствия (апстримы)
def pop_upstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    cores = Core.objects.all()
    upstream = Pop.objects.get(pk=pk).core_set.all()
    context = {'pop': pop, 'upstream': upstream, 'cores': cores}
    return render(request, 'inventory/pop_upstreams.html', context)

def pop_upstreams_remove(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.remove(Core.objects.get(pk=corepk))
    return redirect('pop_list')

def pop_upstreams_add(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.add(Core.objects.get(pk=corepk))
    return redirect('pop_list')

# На Точках присутствия (даунстримы)
def pop_downstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    customers = Customer.objects.all()
    downstream = Pop.objects.get(pk=pk).customer_set.all()
    context = {'pop': pop, 'downstream': downstream, 'customers': customers}
    return render(request, 'inventory/pop_downstreams.html', context)

def pop_downstreams_remove(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.remove(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.remove(Pop.objects.get(pk=poppk))
    return redirect('pop_list')

def pop_downstreams_add(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.add(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.add(Pop.objects.get(pk=poppk))
    return redirect('pop_list')

# На Клиентах (апстримы)
def customer_upstreams(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    pops = Pop.objects.all()
    upstream = Customer.objects.get(pk=pk).pop_set.all()
    context = {'customer': customer, 'upstream': upstream, 'pops': pops}
    return render(request, 'inventory/customer_upstreams.html', context)

def customer_upstreams_remove(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.remove(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.remove(Pop.objects.get(pk=poppk))
    return redirect('customer_list')

def customer_upstreams_add(request, customerpk, poppk):
    Pop.objects.get(pk=poppk).customer_set.add(Customer.objects.get(pk=customerpk))
    Customer.objects.get(pk=customerpk).pop_set.add(Pop.objects.get(pk=poppk))
    return redirect('customer_list')

# Клиенты
# Отобразить всех клиентов
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'inventory/customer_list.html', {'customers': customers})

# Отображение данных по клиенту
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    upstream = Customer.objects.get(pk=pk).pop_set.all()
    context = {'customer': customer, 'upstream': upstream}
    return render(request, 'inventory/customer_detail.html', context)

# Создать клиента
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
def customer_remove(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')

#Редактировать детали подключения клиента
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
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'inventory/device_list.html', {'devices': devices})

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    context = {'device': device}
    return render(request, 'inventory/device_detail.html', context)

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
def device_remove(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('device_list')
