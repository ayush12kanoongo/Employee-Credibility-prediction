
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url 
# from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
    # url('$',views.index, name = 'Homepage'),
    # url('predictMPG',views.predictMPG, name = 'predictMPG'),
]
