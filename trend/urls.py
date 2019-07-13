from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

url(r'^$',views.home,name='home'),
 url(r'^profile/(\d+)$',views.profile,name='profile'),
 url(r'^profile/update/(\d+)$',views.update_profile,name='update_profile'),
 url(r'^category/(\w+)$',views.product_category,name="category"),
 url(r'^product/(\d+)$',views.single_product,name='single_product'),
 url(r'favourite/(\d+)$',views.favourite,name='favourite'),
 url(r'^trend$',views.trend,name='trend'),
 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)