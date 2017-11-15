# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

def home(request):
	num = None
	some_list = [ random.randint(0, 100000), random.randint(0, 100000),random.randint(0, 100000)]
	condition_bool_item = False

	if condition_bool_item:
		num = random.randint(0, 100000)
	context = {"html":"context_variable",
			 "num":num,
	 		 "some_list":some_list}
	return render(request, "home.html",context )

def about(request):
	
	context = {}
	return render(request, "about.html",context )

def contact(request):
	
	context = {}
	return render(request, "contact.html",context )



# class ContactView(View):
# 	"""docstring for ContactView"""

# 	def get(self, request, *args, **kwargs):
# 		context = {}
# 		return render(request, "contact.html",context )


#class HomeView(TemplateView):
	

# class AboutView(TemplateView):
# 	template_name = 'about.html'


# class ContactView(TemplateView):
# 	template_name = 'contact.html'		




def restaurant_createview(request):
	
	form = RestaurantLocationCreateForm(request.POST or None)
	errors=None
	
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurants")

	if form.errors:
		print form.errors	
		errors = form.errors
	template_name='restaurants/form.html'
	context={"form":form, "errors":errors} #can pass in the form itself so that we dont have to write the fields again in the html
	return render(request, template_name, context)



def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context={
		"object_list":queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	#template_name='restaurants/restaurants_list.html'
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:	
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact = slug)|
				Q(category__icontains = slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset


class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	print self.kwargs
	# 	context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
	# 	print context
	# 	return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id = rest_id)
	# 	return obj
		

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = "/restaurants/"