from django.contrib.auth.models import User, Group
from .models import SalleReunion, Reservation
from rest_framework import viewsets
from .serializers import UserSerializer, ReservationSerializer, SalleSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class SalleViewSet(viewsets.ModelViewSet):
    queryset = SalleReunion.objects.all()
    serializer_class = SalleSerializer
