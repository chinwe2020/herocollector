from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('heros/', views.heros_index, name='index'),
    path('heros/<int:hero_id>/', views.heros_detail, name='detail'),
    path('heros/create/', views.HeroCreate.as_view(), name='heros_create'),
    path('heros/<int:pk>/update/', views.HeroUpdate.as_view(), name='heros_update'),
    path('heros/<int:pk>/delete/', views.HeroDelete.as_view(), name='heros_delete'),
    path('heros/<int:hero_id>/add_fighting/', views.add_fighting, name='add_fighting'),
      path('heros/<int:hero_id>/assoc_power/<int:power_id>/', views.assoc_power, name='assoc_power'),
]