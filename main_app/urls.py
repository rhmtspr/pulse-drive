from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("car_detail/<int:car_id>", views.car_detail, name="car_detail"),
    path("transaction/<int:car_id>", views.create_transaction, name="create_transaction"),
    path("transaction_detail/", views.transaction_detail, name="transaction_detail"),
    path("delete_transaction/<int:transaction_id>", views.delete_transaction, name="delete_transaction"),
    path("generate_bill/", views.generate_bill, name="generate_bill"),
    path("pdf_report/", views.pdf_report_create, name="pdf_report")
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)