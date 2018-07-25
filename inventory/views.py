from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from .models import Pop, Core
from .forms import PopForm, CoreForm

# Create your views here.
# Отобразить точки присутствия
def pop_list(request):
    pops = Pop.objects.all()
    return render(request, 'inventory/pop_list.html', {'pops': pops})

# Отображение данных по точке присутствия
def pop_detail(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    upstream = Pop.objects.get(pk=pk).core_set.all()
    context = {'pop': pop, 'upstream': upstream}
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
    downstream = Core.objects.get(pk=pk).pop_set.all()
    context = {'core': core, 'downstream': downstream}
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

#Удалить точку присутствия
def core_remove(request, pk):
    core = get_object_or_404(Core, pk=pk)
    core.delete()
    return redirect('core_list')

# Связки
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

# На Точках присутствия (апстримы)
def pop_downstreams(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    cores = Core.objects.all()
    upstream = Pop.objects.get(pk=pk).core_set.all()
    context = {'pop': pop, 'upstream': upstream, 'cores': cores}
    return render(request, 'inventory/pop_downstreams.html', context)

def pop_downstreams_remove(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.remove(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.remove(Core.objects.get(pk=corepk))
    return redirect('pop_list')

def pop_downstreams_add(request, poppk, corepk):
    Core.objects.get(pk=corepk).pop_set.add(Pop.objects.get(pk=poppk))
    Pop.objects.get(pk=poppk).core_set.add(Core.objects.get(pk=corepk))
    return redirect('pop_list')
