from django.urls import path
from . import views

#url conf module
urlpatterns = [


    # send /user to index
    path('', views.user_home, name='rec_home'),
]