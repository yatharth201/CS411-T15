from django.urls import include, path
from . import views
app_name = 'dashboard'
urlpatterns = [
    path('', views.gotoDash, name='dashPage'),

]
