from django.urls import path
from .views import salle_detail_view, salle_list_view, salle_update_view, salle_delete_view, salle_create_view


urlpatterns = [
    path('', salle_list_view, name='salle-list'),
    path('<int:salle_number>/', salle_detail_view, name='salle-details'),
    path('<int:salle_number>/update/',
         salle_update_view, name='salle-update'),
    path('<int:salle_number>/delete/',
         salle_delete_view, name='salle-delete'),
    path('create/', salle_create_view, name='salle-create'),
]