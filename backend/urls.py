from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('',views.home, name='homepage'),
    path('single/<slug:slug>',views.single, name = 'single'),
    path("about/", views.about, name = 'about')

]
