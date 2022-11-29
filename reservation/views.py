from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import requests
from API.models import Reservation
from .forms import CreateReservationModelForm
from django.contrib.auth.models import User


def reservation_list_view(request):
    if request.GET.get('user-filter'):
        user_filter = request.GET.get('user-filter')
        queryset = Reservation.objects.filter(reservation_user=user_filter)
    else:
        queryset = Reservation.objects.all()
    user_list = User.objects.all()
    title = "  liste de Reservations"
    template_name = 'reservation/list.html'
    context = {
        'title': title,
        'object_list': queryset,
        'user_list': user_list
    }
    return render(request, template_name, context)


@login_required
def reservation_create_view(request):
    template_name = 'reservation/create.html'
    form = CreateReservationModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            user = request.user
            data.update({'reservation_user': int(user.id)})
            response = requests.post(
                'http://localhost:8000/api/reservation/', data=data)
            content = response.content
            return redirect('/reservations/')
    context = {
        "title": "Créer  nouvelle reservation",
        "form": form
    }
    return render(request, template_name, context)


def reservation_detail_view(request, id, *numero_salle):
    title = "Détails salle reunion numero " + str(numero_salle) 
    obj = get_object_or_404(Reservation, id=id)
    template_name = 'reservation/detail.html'
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)


@login_required
def reservation_update_view(request, *numero_salle, id):
    title = "Mise a jour de salle de reunion numero  " + str(numero_salle) 
    obj = get_object_or_404(Reservation, id=id)
    form = CreateReservationModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/reservations')
    template_name = 'reservation/create.html'
    context = {
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def reservation_delete_view(request, *numero_salle, id):
    title = "supprimer  salle réunion numero " + str(numero_salle)
    obj = get_object_or_404(Reservation, id=id)
    template_name = 'reservation/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/reservations')
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)
