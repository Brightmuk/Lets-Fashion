from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

url(r'^$',views.home,name='home'),
 url(r'^profile/(\d+)$',views.profile,name='profile'),
 url(r'^profile/update/(\d+)$',views.update_profile,name='update_profile'),
 url(r'^category/(\d+)',views.product_category,name="category")   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)