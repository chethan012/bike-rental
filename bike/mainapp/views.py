
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
from .models import Bike

def HomeView(request):
  template = 'home.html'
  context = {
    
  }
  return render(request ,template,context)

def aboutview(request):
  template = 'about.html'
  context = {
    
  }
  return render(request, template, context)

def contactview(request):
  template = 'contact.html'
  context = {
    
  }
  return render(request, template, context)

def bikelistview(request):
  template = 'bikelist.html'
  context = {
    'bikes' : Bike.objects.all()
  }
  return render(request, template, context)

class AddBike(CreateView):
  model = Bike
  template_name = 'addbike.html'
  fields = '__all__'
  success_url = '/'
  
class UpdateBike(UpdateView):
  model = Bike
  template_name = 'update_bike.html'
  fields = '__all__'
  success_url = '/'
  
class DeleteBike(DeleteView):
  model = Bike
  template_name = 'delete_bike.html'
  fields = '__all__'
  success_url = '/'
  
class BikeDetails(DetailView):
  model = Bike
  template_name = 'bike_details.html'
  fields = '__all__'
  success_url = '/'
  
def searchView(request):
    query = request.GET.get('q')
    result_bikes = Bike.objects.filter(model_name__icontains = query)
    context = {
        'query' : query,
        'bikes' : result_bikes
    }
    template = 'search_results.html'

    return render(request, template, context)