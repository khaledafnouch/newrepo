from django.contrib.auth.models import User, Group
from django.db.models.fields import DateField, DurationField, TimeField
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import SalleReunion, Reservation


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'password',
            'email',
            'groups',
            'id',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class SalleSerializer(serializers.ModelSerializer):
    numero_salle = serializers.IntegerField()
    capacity = serializers.IntegerField()

    class Meta:
        model = SalleReunion
        fields = [
            'url',
            'numero_salle',
            'capacity',
        ]


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'url',
            'numero_salle',
            'reservation_date',
            'reservation_time',
            'reservation_duration',
            'reservation_user',
            'id',
        ]
