# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader

from parkhealth.settings import MEDIA_URL, BASE_URL
from parkhealth.app_main.models import MedicalStaff, Specialty

def index(request):
    return render_to_response('main/home.html', 
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
            'MENU':menu(section="home"), })


def department(request, page):
    html_page = "department/%s.html" % (page)

    specialties = Specialty.objects.filter(is_menu=True)
    index = 0
    cutoff = False
    for s in specialties:
            if cutoff == False:
                    index += 1
            if s.handle == page:
                    cutoff = True

    specialty = Specialty.objects.get(handle=page)
    medical_staff = MedicalStaff.objects.filter(specialty=specialty).order_by("name_last")

    return render_to_response(html_page, 
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
            'specialty':specialty, 'medical_staff':medical_staff,
            'MENU':menu(section="dept", subsection=page), })

def staff(request, section):
    html_page = "staff/%s.html" % (section)

    medical_staff = MedicalStaff.objects.filter(staff_listing=True).order_by('name_last')

    return render_to_response(html_page, 
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
            'medical_staff':medical_staff,
            'MENU':menu(section), })

def staff_bio(request, section, first, last):
    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())
    subsection = "bio"

    html_page = "staff/%s/%s.html" % (section, bio.handle())

    return render_to_response(html_page, 
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
            'MENU':menu(section, subsection, bio), })

def community(request, section):
    html_page = "community/%s.html" % (section)

    return render_to_response(html_page,
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL,
            'MENU':menu(section="community", subsection="news"), })
                
def directions(request):
    html_page = "main/directions.html"

    return render_to_response(html_page,
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL,
            'MENU':menu(section="directions"), })

def insurance(request):
    html_page = "main/insurance.html"

    return render_to_response(html_page,
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL,
            'MENU':menu(section="insurance"), })

def contact(request):
    html_page = "main/contact.html"

    return render_to_response(html_page,
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL,
            'MENU':menu(section="contact"), })

def about(request):
    html_page = "main/about.html"

    return render_to_response(html_page,
        { 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
            'MENU':menu(section="about"), })

def menu(section="", subsection="", bio=""):
    specialties = Specialty.objects.filter(is_menu=True)
    t = loader.get_template('main/menu.html')
    c = Context({ 'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 'specialties':specialties, 
        'section':section, 'subsection':subsection, 'bio':bio})
                        
    return t.render(c)

#def menu(request, section="", subsection=""):
#    specialties = Specialty.objects.filter(is_menu=True)
#    
#    return render_to_response('main/menu.xml', 
#                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
#                    'specialties':specialties, 
#                    'section':section, 'subsection':subsection})

#def menu_bio(request, staff_type='medical', first='yakov', last='beim'):
#    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())
#
#    section = "bio"
#    subsection = "medical"
#
#    specialties = Specialty.objects.filter(is_menu=True)
#    return render_to_response('main/menu.xml', 
#                    {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
#                        'bio':bio, 'specialties':specialties,
#                        'section':section, 'subsection':subsection})
