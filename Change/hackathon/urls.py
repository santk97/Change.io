
from views import start_view,singnup_view,like_view,indexview1,login_user,logout_view,activate,swatchh_signup,swatch_login,dashboard

from views import singnup_view,indexview1,login_user,logout_view,activate,swatchh_signup,swatch_login,dashboard , feedback,password
from django.conf.urls import url
urlpatterns = [
    url(r'^$', indexview1),
    url(r'^signup/',singnup_view),
   # url(r'^index/',indexview1),
    url(r'^login/',login_user),
    url(r'^logout/',logout_view),
    url(r'^activate/',activate),
    url(r'^like/', like_view),
    url(r'^activate/',activate),
    url(r'^swatchh_signup/',swatchh_signup),
    url(r'^swatchh_login/',swatch_login),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^password/',password),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^password/',password),

]