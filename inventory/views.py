from django.shortcuts import render, get_object_or_404, redirect
from .models import Pop
from .forms import PopForm

# Create your views here.
# Отобразить точки присутствия
def pop_list(request):
    pops = Pop.objects.all()
    return render(request, 'inventory/pop_list.html', {'pops': pops})

# Отображение данных по точке присутствия
def pop_detail(request, pk):
    pop = get_object_or_404(Pop, pk=pk)
    return render(request, 'inventory/pop_detail.html', {'pop': pop})

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
