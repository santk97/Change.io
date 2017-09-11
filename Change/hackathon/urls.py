from django.conf.urls import url
from views import singnup_view,indexview1,login_user,logout_view

urlpatterns = [
    url(r'^$', indexview1),
    url(r'^signup/',singnup_view),
    url(r'^index/',indexview1),
    url(r'^login/',login_user),
    url(r'^logout/',logout_view),
]