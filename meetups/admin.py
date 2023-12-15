from django.contrib import admin

from meetups.models import Meetup, Location, Participant


# Register your models here.

@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ['title', "date", 'location', "updated_on", "created_on"]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ["title", 'location', "updated_on", "created_on", "location"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(Participant)
class AttendantAdmin(admin.ModelAdmin):
    list_filter = ["email"]
