from django.shortcuts import render

from medetsin_app.models import Jamoa

# Create your views here.

def tort(request):
    return render(request, '404.html')


def about_funk(request):
    return render(request, 'about.html')


def blog_mason(request):
    return render(request, 'blog-masonry.html')


def kontak(request):
    return render(request, 'contacts.html')


def depart(request):
    return render(request, 'departments.html')


def faqq(request):
    return render(request, 'faq.html')


def grid_galery(request):
    return render(request, 'grid-gallery.html')


def indexx(request):
    return render(request, 'index.html')



def make_an(request):
    return render(request, 'make-an-appointment.html')



def search_r(request):
    return render(request, 'search-results.html')



def servicess(request):
    return render(request, 'services.html')


def single(request):
    return render(request, 'single-post.html')


def team_memr(request):
    return render(request, 'team-member.html')


def team_(request):
    rasm=Jamoa.objects.all()
    return render(request, 'team.html',{"rasmlar":rasm})
    
    
def time(request):
    return render(request, 'timetable.html')