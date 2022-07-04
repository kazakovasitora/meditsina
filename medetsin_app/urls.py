from django.urls import path
from .views import *

urlpatterns = [
    path('404', tort, name='404'),
    path('about_/', about_funk, name='about'),
    path('blog_/', blog_mason, name='blog'),
    path('kontakts_/', kontak, name='kontak'),
    path('departmen/', depart, name='department'),
    path('faq/', faqq, name='faqq'),
    path('grid/', grid_galery, name='grid_galery'),
    path('', indexx, name='index_'),
    path('make_/', make_an, name='make_an'),
    path('search_/', search_r, name='search_result'),
    path('servic/', servicess, name='service'),
    path('singgle_/', single, name='singlee'),
    path('team_m/', team_memr, name='team_me'),
    path('team_/', team_, name='team'),
    path('time_tab/', time, name='time_table'),
]