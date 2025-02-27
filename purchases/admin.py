from django.contrib import admin
from .models import Branch, Product, BranchProductHistory, PurchaseRequest, ApprovedPurchase, PurchaseOrder

admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(BranchProductHistory)
admin.site.register(PurchaseRequest)
admin.site.register(ApprovedPurchase)
admin.site.register(PurchaseOrder)