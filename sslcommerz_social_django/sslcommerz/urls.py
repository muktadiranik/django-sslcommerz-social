from django.urls import path
from .views import SSLCOMMERZ_GATEWAY, _sslcommerz_success, _sslcommerz_failed, _sslcommerz_cancel


app_name = "sslcommerz"
urlpatterns = [
    path("", SSLCOMMERZ_GATEWAY.as_view(), name="sslcommerz"),
    path("success/", _sslcommerz_success, name="sslcommerz-success"),
    path("fail/", _sslcommerz_failed, name="sslcommerz-fail"),
    path("cancel/", _sslcommerz_cancel, name="sslcommerz-cancel"),
]
