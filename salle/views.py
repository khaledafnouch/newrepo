from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from API.models import SalleReunion
from .forms import CreateSalleModelForm


def salle_list_view(request):
    queryset = SalleReunion.objects.all()
    #print(queryset)
    title = "liste salle de réunion"
    template_name = 'salle/list.html'
    context = {
        'title': title,
        'object_list': queryset
    }
    return render(request, template_name, context)


@login_required
def salle_create_view(request):
    template_name = 'salle/create.html'
    form = CreateSalleModelForm(request.POST or None)
    if form.is_valid():

        form.user = request.user
        form.save()
        form = CreateSalleModelForm()
        return redirect('/salles')
    context = {
        "title": "Créer nouvelle salle",
        "form": form
    }
    return render(request, template_name, context)


def salle_detail_view(request, numero_salle):
    title = " détails de la salle"+ str(numero_salle) 
    obj = get_object_or_404(SalleReunion, numero_salle=numero_salle)
    template_name = 'salle/detail.html'
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def salle_update_view(request, numero_salle):
    title = "mise à jour salle reunion  numero : " + str(numero_salle) 
    obj = get_object_or_404(SalleReunion, numero_salle=numero_salle)
    form = CreateSalleModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/salles')
    template_name = 'salle/create.html'
    context = {
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def salle_delete_view(request, numero_salle):
    title = "salle " + str(numero_salle) + " supprimée"
    obj = get_object_or_404(SalleReunion, numero_salle=numero_salle)
    template_name = 'salle/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/salles')
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)
