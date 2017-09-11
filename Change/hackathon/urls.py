from django.conf.urls import url

from views import activate, swatchh_signup, swatch_login, dashboard, feedback, password, comment_view, logout_view, \
    login_user, singnup_view, index
from views import start_view, post_view
urlpatterns = [
    url(r'^$',index),
    url(r'^signup/',singnup_view),
   # url(r'^index/',indexview1),
    url(r'^login/',login_user),
    url(r'^logout/',logout_view),
    url(r'^activate/',activate),

    url(r'^startproject/',start_view),

    url(r'^activate/',activate),
    url(r'^swatchh_signup/',swatchh_signup),
    url(r'^swatchh_login/',swatch_login),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^post/', post_view),
url(r'^comment/', comment_view),
    url(r'^password/',password),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^password/',password),

]