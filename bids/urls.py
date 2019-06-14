from django.conf.urls import url
from bids import views
from bids.views import StatusHistoryView

urlpatterns = [
    url(r'^bidsimport/$', views.bidsimport, name='bidsimport'),
    url(r'^bids/$', views.bids, name='bids'),
    url(r'^bids/(?P<bids_filter>\d+)/$', views.bids, name='bids'),
    url(r'^bidsedit/(?P<edit_id>\d+)/$', views.bidsedit, name='bidsedit'),
    url(r'^bidsedit/$', views.bidsedit, name='bidsedit'),
    url(r'^doubleedit/$', views.doubleedit, name='doubleedit'),
    url(r'^doubleedit/(?P<edit_id>\d+)/$', views.doubleedit, name='doubleedit'),
    url(r'^bidsadd/$', views.bidsadd, name='bidsadd'),
    url(r'^bidsdouble/$', views.bidsdouble, name='bidsdouble'),
    url(r'^status_history/(?P<edit_id>\d+)/$', StatusHistoryView.as_view(), name='status_history'),
    url(r'^status_history/$', StatusHistoryView.as_view(), name='status_history'),
]
