from django.conf.urls import url
from django.conf.urls import include

# this does the static file loading when in dev mode, not needed for production
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import HomeView
from .views import NotFoundView
from accounts.views import AccountDetailView

urlpatterns = [
    url(
        r'^$',
        HomeView.as_view(),
        name='home',
    ),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(
        r'^(?P<username>[-\w.@]+)/$',
        AccountDetailView.as_view(),
        name='account_detail',
    )
]
# add the static file patterns to url patterns
urlpatterns += staticfiles_urlpatterns()

handler404 = NotFoundView.as_view()
