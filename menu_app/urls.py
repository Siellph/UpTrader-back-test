from django.urls import path
from menu_app.views import home

urlpatterns = [
    path('', home, name='main_menu'),
    path('main_menu/first/', home, name='first_main_menu'),
    path('main_menu/second/', home, name='second_main_menu'),
    path('home/', home, name='home'),
    path('home/one/', home, name='one_home'),
    path('home/two/', home, name='two_home'),
    path('home/three/', home, name='three_home'),
    path('home/four/', home, name='four_home'),
]
