from django.contrib import admin
from django.urls import path
from .views import PurchaseRequestCreateView

urlpatterns = [
    path('request/new/', PurchaseRequestCreateView.as_view(), name = 'purchase_request_create'),
]
