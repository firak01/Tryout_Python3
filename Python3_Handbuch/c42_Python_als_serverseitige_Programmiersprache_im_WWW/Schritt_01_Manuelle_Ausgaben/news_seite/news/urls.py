from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.meldungen, name='meldungen'),
    path('<int:meldungs_id>/', views.meldungen_detail, name='meldungen_detail'),
]
