#Creating Endpoints
#In words of API Endpoints means urls

from django.urls import path
from . import views
from .views import EnrolList, EnrolDetail


urlpatterns = [
    path("",EnrolList.as_view()),
    path("<int:pk>",EnrolDetail.as_view()),
    path('get/python',views.getPython,name = 'getdata'),
    path('get/java',views.getJava,name = 'getdata'),
    path('get/testing',views.getTesting,name = 'getdata'),
    path('post/',views.insertData,name = 'insertdata'),
    
]