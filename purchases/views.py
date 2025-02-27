from django.views import View
from django.shortcuts import render, redirect
from .models import PurchaseRequest, Product
from .forms import PurchaseRequestForm

class PurchaseRequestCreateView(View):
    template_name = "PurchaseRequestForm.html"

    def get(self, request):
        form = PurchaseRequestForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = PurchaseRequestForm(request.POST)
        if form.is_valid():
            purchase_request = form.save()
            
            # ذخیره مقدار تعداد موجودی برای هر محصول
            for product in form.cleaned_data["products"]:
                quantity = request.POST.get(f"quantity_{product.id}", 0)
                purchase_request.products.add(product, through_defaults={'current_stock': quantity})
            
            return redirect("/")
        return render(request, self.template_name, {"form": form})