from django.urls import path
from . views import *
from .import views


urlpatterns= [
     path('create/',tourist_create.as_view(),name='create'),
     path('detail/<int:pk>/',tourist_detail.as_view(),name='detail'),
     path('update/<int:pk>/',tourist_update.as_view(),name='update'),
     path('delete/<int:pk>/',touristdelete.as_view(),name='delete'),




     path('create_place/',views.create_tourist_places,name='create_place'),
     path('place_detail/<int:id>/',views.tourist_details,name='place_detail'),
     path('',views.index,name='index'),
     path('update_tour/<int:id>/',views.destination_update,name='update_tour'),
     path('update_details/<int:id>/',views.destination_updation_details,name='update_details'),
     path('place_delete/<int:id>/',views.destination_delete,name='place_delete')

]