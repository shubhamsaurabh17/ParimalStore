from django import forms
from TestApp.models import Enquiry, RC, Product, Feedback
class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields="__all__"


class RCForm(forms.ModelForm):
    class Meta:
        model=RC
        fields="__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
