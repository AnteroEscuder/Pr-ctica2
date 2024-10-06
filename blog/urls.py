from django.urls import path

from blog import views


urlpatterns = [
    path('coche_list', views.coche_list, name="coche_list"),
    path('propietario_list', views.propietario_list, name="propietario_list"),
]