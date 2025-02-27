from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name="managed_branch")

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class BranchProductHistory(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    last_purchased_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('branch', 'product')

    def __str__(self):
        return f"{self.branch.name} - {self.product.name} (Last: {self.last_purchased_at})"
        
class PurchaseRequest(models.Model):
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='PurchaseRequestItem')

    def __str__(self):
        return f"Request from {self.branch} - {self.created_at}"

class PurchaseRequestItem(models.Model):
    request = models.ForeignKey(PurchaseRequest, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_stock = models.PositiveIntegerField()  # مقدار موجودی که مدیر شعبه وارد می‌کند
    required_quantity = models.PositiveIntegerField(null=True, blank=True)  # مقدار مورد نیاز که ادمین وارد می‌کند

    def __str__(self):
        return f"{self.product.name} in request {self.request.id}"
class ApprovedPurchase(models.Model):
    request = models.OneToOneField(PurchaseRequest, on_delete=models.CASCADE)
    final_quantity = models.PositiveIntegerField()
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.branch} - {self.created_at}"

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    approved_purchases = models.ManyToManyField(ApprovedPurchase)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.status}"
        
