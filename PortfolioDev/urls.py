from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name='index'),
	path("ajax_test", views.ajax_test, name='ajax_test'),
 
 
]