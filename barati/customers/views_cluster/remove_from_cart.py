from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

class Remove_From_Cart(View):
   try:
      def __init__(self):
         self.template_name = 'customers/cart.html'
         self.wishlist_list = []
      
      def get_context_data(self, **kwargs):
         context = {}
         return context
         
      def post(self, request, **kwargs):
         ref_id = kwargs['ref_id']
         card_prod_to_delete = m.Cart.objects.filter(ref_id=ref_id)
         for prod in card_prod_to_delete:
            prod.delete()
         message = "success_remove_from_cart"
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
