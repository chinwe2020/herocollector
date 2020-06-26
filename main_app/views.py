from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hero, Power
from .forms import FightingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def heros_index(request):
    heros = Hero.objects.all()
    return render(request, 'heros/index.html', {'heros': heros})

def heros_detail(request, hero_id):
  hero = Hero.objects.get(id=hero_id)
  powers_hero_doesnt_have = Power.objects.exclude(id__in = hero.powers.all().values_list('id'))
  fighting_form = FightingForm()
  return render(request, 'heros/detail.html', { 
    'hero': hero, 
    'fighting_form': fighting_form,
    'powers': powers_hero_doesnt_have
   })

def add_fighting(request, hero_id):
  form = FightingForm(request.POST)
  if form.is_valid():
    new_fighting = form.save(commit=False)
    new_fighting.hero_id = hero_id
    new_fighting.save()
  return redirect('detail', hero_id=hero_id)

class HeroCreate(CreateView):
  model = Hero
  fields = '__all__'
 
class HeroUpdate(UpdateView):
  model = Hero
  fields = ['superpower', 'weapon', 'weakness']

class HeroDelete(DeleteView):
  model = Hero
  success_url = '/heros/'

class PowerList(ListView):
  model = Power

class PowerDetail(DetailView):
  model = Power

class PowerCreate(CreateView):
  model = Power
  fields = '__all__'

class PowerDelete(DeleteView):
  model = Power
  success_url = '/powers/'

def assoc_power(request, hero_id, power_id):
  Hero.objects.get(id=hero_id).powers.add(power_id)
  return redirect('detail', hero_id=hero_id)