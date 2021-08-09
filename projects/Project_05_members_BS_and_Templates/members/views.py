from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Announcement, Member, Conference, Event
from datetime import datetime


####################
# Class-based ListView ... populate:
# template_name:  the HTML template to use
# context_object_name:  the variable name inside the template
# get_queryset(self): the data to populate the context_object_name
####################
class AnnouncementsView(generic.ListView):
    template_name = 'members/announcement_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Announcement.objects.all()


#####################
# Class-based DetailView ... populate:
# template_name:  the HTML template to use
# model:  the table to use (pk is part of URL)
#####################


class AnnouncementView(generic.DetailView):
    model = Announcement
    template_name = 'members/announcement_results.html'


class MembersView(generic.ListView):
    template_name = 'members/member_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Member.objects.all()


class MemberView(generic.DetailView):
    model = Member
    template_name = 'members/member_results.html'


class ConferencesView(generic.ListView):
    template_name = 'members/conference_index.html'
    context_object_name = 'list'

    # list of all the conferences (includes full row of data, name, description, ...)
    def get_queryset(self):
        return Conference.objects.all()


class ConferencesMemberCountView(generic.ListView):
    template_name = 'members/conference_member_count.html'
    context_object_name = 'list'

    # list of name and count of all distinct conferences, and the count of members in that conference
    def get_queryset(self):
        print(Conference.objects.values('name').order_by('name').annotate(count=Count('members')))
        return Conference.objects.values('name').order_by('name').annotate(count=Count('members'))


class ConferenceView(generic.DetailView):
    model = Conference
    template_name = 'members/conference_results.html'


class EventsView(generic.ListView):
    template_name = 'members/event_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'members/event_results.html'
