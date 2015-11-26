from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

#@login_required(login_url='/auth/login/')
class Dashboard(View):
   try:
      def __init__(self):
         self.template_name = 'customers/index.html'
         
      def get_context_data(self, **kwargs):
         query = "select id, name from venue_types"
         venue_types = m.Venue_Types.objects.raw(query)
         
         query = "select id, name from card_types"
         card_types = m.Card_Types.objects.raw(query)
         
         query = "select id, name from beautician_types"
         beautician_types = m.Beautician_Types.objects.raw(query)
         
         query = "select id, name from music_types"
         music_types = m.Music_Types.objects.raw(query)
         
         query = "select id, name from gift_types"
         gift_types = m.Gift_Types.objects.raw(query)
         
         query = "select id, name from photo_types"
         photo_types = m.Photo_Types.objects.raw(query)
         
         query = "select id, name from video_types"
         video_types = m.Video_Types.objects.raw(query)
         
         query = "select id, name from bakery_types"
         bakery_types = m.Bakery_Types.objects.raw(query)
         
         query = "select id, name from ghodi_bagghi_types"
         ghodi_bagghi_types = m.Ghodi_Bagghi_Types.objects.raw(query)
         
         query = "select id, name from band_types"
         band_types = m.Band_Types.objects.raw(query)
         
         query = "select id, name from mehendi_types"
         mehendi_types = m.Mehendi_Types.objects.raw(query)
         
         query = "select id, name from fireworks_types"
         fireworks_types = m.Fireworks_Types.objects.raw(query)
         
         query = "select id, name from tent_types"
         tent_types = m.Tent_Types.objects.raw(query)
         
         context = {\
         'venue_types' : venue_types, 'card_types' : card_types, 'beautician_types' : beautician_types,\
         'gift_types' : gift_types, 'photo_types' : photo_types,\
         'video_types' : video_types, 'bakery_types' : bakery_types, 'ghodi_bagghi_types' : ghodi_bagghi_types,\
         'band_types' : band_types, 'mehendi_types' : mehendi_types, 'fireworks_types' : fireworks_types,\
         'tent_types' : tent_types, 'music_types' : music_types \
         }
         return context
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_context_data()
         return render(request, self.template_name, context_dict)
   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
