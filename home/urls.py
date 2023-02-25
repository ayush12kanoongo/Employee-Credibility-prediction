from django.urls import path
#from django.urls import path


from home import views

urlpatterns = [
    path('',views.main, name = 'main'),
    path('predictMPG',views.predictMPG, name = 'predictMPG'),
]
