from django.db import models
from django.contrib import admin

# Create your models here.

class Degree(models.Model):
    name = models.CharField(max_length=1000)
    acronym = models.CharField(max_length=200)
    priority = models.IntegerField()

    def __unicode__(self):
        return self.acronym

    class Meta:
        ordering = ["acronym"]

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    menu = models.CharField(max_length=100, blank=True)
    is_menu = models.BooleanField()
    handle = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class MedicalStaff(models.Model):
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    middle_inital = models.CharField(max_length=1, blank=True)

    has_bio = models.BooleanField()
    staff_listing = models.BooleanField()

    degrees = models.ManyToManyField('Degree')
    specialty = models.ManyToManyField('Specialty')

    def handle(self):
        return "%s_%s" % (self.name_first.lower(), self.name_last.lower())

    def get_degrees(self):
        return self.degrees.all().order_by('priority')

    def get_specialties(self):
        return self.specialty.all()

    def __unicode__(self):
        if self.middle_inital == '':
            return "%s %s" % (self.name_first, self.name_last)

        return "%s %s. %s" % (self.name_first, self.middle_inital, self.name_last)


