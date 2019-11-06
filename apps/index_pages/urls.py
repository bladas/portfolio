
from django.conf.urls import url

from apps.index_pages.views import Home,Contact,Galery,Pricing,Services

app_name = 'home'
urlpatterns = [

    url(r'^$', Home.as_view(), name='home'),
    url(r'contact/', Contact.as_view(), name='contact'),
    url(r'portfolio/', Galery.as_view(), name='galery'),
    url(r'pricing/', Pricing.as_view(), name='pricing'),
    url(r'services/', Services.as_view(), name='services'),


]