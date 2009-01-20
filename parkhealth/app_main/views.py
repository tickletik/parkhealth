# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from parkhealth.settings import MEDIA_URL, BASE_URL
from parkhealth.app_main.models import MedicalStaff

def index(request):
    return render_to_response('main/home.html', {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL})

def department(request, page='dept'):
    html_page = "department/%s.html" % (page)
    return render_to_response(html_page, {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL})

def staff(request, section):
    html_page = "staff/%s.html" % (section)
    
    medical_staff = MedicalStaff.objects.filter(staff_listing=True).order_by('name_last')

    return render_to_response(html_page, {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL, 'medical_staff':medical_staff})

def staff_bio(request, section, first, last):
    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())

    html_page = "staff/%s/%s.html" % (section, bio.handle())
    return render_to_response(html_page, {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL, "bio":bio})

def menu(request):
    return render_to_response('main/menu.xml', {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL})

def menu_bio(request, staff='medical', first="yakov", last="beim"):
    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())

    return render_to_response('main/menu.xml', {"MEDIA_URL":MEDIA_URL, "BASE_URL":BASE_URL, "staff":staff, "bio":bio})
