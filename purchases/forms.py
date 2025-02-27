from django import forms
from .models import PurchaseRequest, Product

class PurchaseRequestForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for product in Product.objects.all():
            field_name = f"quantity_{product.id}"
            self.fields[field_name] = forms.IntegerField(
                label=f"تعداد موجودی {product.name}",
                min_value=0,
                required=False
            )

    class Meta:
        model = PurchaseRequest
        fields = ['products']