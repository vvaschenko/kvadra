from django.conf.urls import url
from bids import views

urlpatterns = [
    url(r'^bidsimport/', views.bidsimport, name= 'bidsimport'),
    url(r'^bids/', views.bids, name='bids'),
    url(r'^bidsedit/(?P<edit_id>\d+)/$', views.bidsedit, name= 'bidsedit'),
    url(r'^bidsedit/', views.bidsedit, name='bidsedit'),
    url(r'^doubleedit/', views.doubleedit, name='doubleedit'),
    url(r'^bidsadd/', views.bidsadd, name='bidsadd'),
    url(r'^bidsdouble/', views.bidsdouble, name='bidsdouble'),
]
