"""
A collection of URLs that should only be viewable when DEBUG=True. Useful for debugging custom error pages
"""

from django.conf import settings
from django.conf.urls import url
from django.views import defaults

app_name = "errorpages"

urlpatterns = [
    url(r"^500/$", defaults.server_error),
    url(r"^403/$", defaults.permission_denied, kwargs={"exception": Exception("Permission denied")} ),
    url(r"^404/$", defaults.page_not_found, kwargs={"exception": Exception("Page not found")}),
]

urlpatterns = urlpatterns if settings.DEBUG else []