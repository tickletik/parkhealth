# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from parkhealth.settings import MEDIA_URL, BASE_URL
from parkhealth.app_main.models import MedicalStaff, Specialty

def index(request):
    menu_index = "1"
    menu_section = "home"
    return render_to_response('main/home.html', 
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'menu_section':menu_section, 'menu_index':menu_index})

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

    menu_index = "2.%i" % index
    menu_section = "department"
    menu_subsection = page

    specialty = Specialty.objects.get(handle=page)
    medical_staff = MedicalStaff.objects.filter(specialty=specialty).order_by("name_last")

    return render_to_response(html_page, 
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'specialty':specialty, 'medical_staff':medical_staff, 
                    'menu_index':menu_index, 'menu_section':menu_section, 'menu_subsection':menu_subsection})

def staff(request, section):
    html_page = "staff/%s.html" % (section)
    
    menu_index = "5"
    if section == "medical":
        menu_index += ".1"
    elif section == "administrative":
        menu_index += ".2"

    menu_section = section 

    medical_staff = MedicalStaff.objects.filter(staff_listing=True).order_by('name_last')

    return render_to_response(html_page, 
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'medical_staff':medical_staff,
                    'menu_index':menu_index, 'menu_section':menu_section})

def staff_bio(request, section, first, last):
    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())

    html_page = "staff/%s/%s.html" % (section, bio.handle())
    menu_section = "bio"
    menu_subsection = "medical"
    menu_index = "5.1.1"

    return render_to_response(html_page, 
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'bio':bio,
                    'menu_index':menu_index, 'menu_section':menu_section, 'menu_subsection':menu_subsection})

def community(request, section=""):
    menu_section="community"
    menu_subsection=""
    menu_index = "3"

    html_page = "community/community.html"

    if section=="gallery":
        menu_index += ".1"
        menu_subsection="gallery"
    
    return render_to_response(html_page,
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'menu_index':menu_index, 'menu_section':menu_section, 'menu_subsection':menu_subsection})

def menu(request, section="", subsection=""):
    specialties = Specialty.objects.filter(is_menu=True)
    
    return render_to_response('main/menu.xml', 
                {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                    'specialties':specialties, 
                    'section':section, 'subsection':subsection})

def menu_bio(request, staff_type='medical', first='yakov', last='beim'):
    bio = MedicalStaff.objects.get(name_last=last.lower().capitalize(), name_first=first.lower().capitalize())

    section = "bio"
    subsection = "medical"

    specialties = Specialty.objects.filter(is_menu=True)
    return render_to_response('main/menu.xml', 
                    {   'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 
                        'bio':bio, 'specialties':specialties,
                        'section':section, 'subsection':subsection})
