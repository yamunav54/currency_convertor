from django.urls import path,include
from . import views
from rest_framework import routers
from .views import RateListViewSet


router = routers.DefaultRouter()
router.register('ratelist',RateListViewSet)
urlpatterns =[
    path('',views.index,name='index'),
    path('getT$("#targetlabel").html(current_var_cur);oken/',views.listTeachers,name='getToken'),
    path('api/',include(router.urls))
]