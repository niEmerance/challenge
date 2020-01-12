from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'new_restaurant/', views.new_restaurant, name = 'new_restaurant'),
    url(r'restaurantDetails/',views.restaurantDetails,name='restaurantDetails'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)