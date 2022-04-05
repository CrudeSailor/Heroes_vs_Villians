from django.urls import path
from . import views

urlpatterns = [
    path('',views.supers_list),
    path('<int:pk>/',views.supers_detail),
]


#127.0.0.1:8000/api/supers/<int:pk>/
#needed to remove path and insert  <int:pk>/
