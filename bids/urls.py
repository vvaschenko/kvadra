from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from bids import views
from bids.views import StatusHistoryView, BidView

urlpatterns = [
    url(r'^bidsimport/$', views.bidsimport, name='bidsimport'),
    url(r'^bids/$', login_required(BidView.as_view()), name='bids'),
    url(r'^bids/(?P<bids_filter>\d+)/$', login_required(BidView.as_view()), name='bids'),
    url(r'^bidsedit/(?P<edit_id>\d+)/$', views.bidsedit, name='bidsedit'),
    url(r'^bidsedit/$', views.bidsedit, name='bidsedit'),
    url(r'^doubleedit/$', views.bidsedit, name='doubleedit'),
    url(r'^doubleedit/(?P<edit_id>\d+)/$', views.bidsedit, name='doubleedit'),
    url(r'^bidsadd/$', views.bidsadd, name='bidsadd'),
    url(r'^bidsdouble/$', login_required(BidView.as_view()), name='bidsdouble'),
    url(r'^status_history/(?P<edit_id>\d+)/$', StatusHistoryView.as_view(), name='status_history'),
    url(r'^status_history/$', StatusHistoryView.as_view(), name='status_history'),
    url(r'^ajax/load-status/$', views.select_status, name='ajax_load_status'),
    url(r'^ajax/add_load-status/$', views.add_select_status, name='add_ajax_load_status'),
]
