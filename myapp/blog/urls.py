from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path("models",views.model,name="model"),
    path('old_url',views.old_url,name="old_url"),
    path('new_url',views.new_url,name="new_url"),
    path('',views.index,name='index'),
    path('details/<str:slug>',views.detail,name='details'),
    path('contacts',views.contact,name="Contact"),
    path('About',views.about,name="About")
]
