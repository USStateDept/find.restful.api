"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView, RedirectView

from rest_framework.authtoken import views
from rest_framework_jwt.views import (
        obtain_jwt_token,
        refresh_jwt_token,
        verify_jwt_token
    )

urlpatterns = [
    # Template Views
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),

    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    # users, administrators, and development document endpoints
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^users/token/', obtain_jwt_token),
    url(r'^users/token-refresh/', refresh_jwt_token),
    url(r'^users/token-verify/', verify_jwt_token),


    # API
    url(r'^categories/', view=include('categories.urls', namespace='categories')),
    url(r'^countries/', view=include('countries.urls', namespace='countries')),
    url(r'^countries/data/', view=include('data.urls', namespace='country_data')),
    url(r'^indicators/', view=include('indicators.urls', namespace='indicators')),
    url(r'^regions/', view=include('regions.urls', namespace='regions')),
    url(r'^regions/data/', view=include('region_data.urls', namespace='region_data')),

    # base url
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Static settings