from django.conf.urls import url
from views import singnup_view,login_user,logout_view

urlpatterns = [
    url(r'^$', singnup_view),
    url(r'^login/',login_user),
    url(r'^logout',logout_view),
]