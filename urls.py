from django.conf.urls.defaults import patterns, include
from django.conf import settings

import twodemo.demoapp.main
import two.userauth.login
import two.userauth.signup
import two.userauth.reset

from two.ol.base import Mapping

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    Mapping("signup", two.userauth.signup.SignupHandler),
    Mapping("login", two.userauth.login.LoginHandler),
    Mapping("reset", two.userauth.reset.ResetHandler),
    Mapping("/", twodemo.demoapp.main.MainHandler),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

