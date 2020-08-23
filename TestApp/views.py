from django.shortcuts import render
from TestApp import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from TestApp.models import Product
import datetime
# Create your views here.
def home_view(request):
    dt=datetime.datetime.now()
    msj1=""
    msj2=""
    h=int(dt.strftime('%H'))
    h=h+5
    if(h>=20):
        msj1="Good Night"
    elif(h>=16):
        msj1="Good Evening"
    elif(h>=12):
        msj1="Good Afternoon"
    else:
        msj1="Good Morning"
    if(h>=7 and h<=19):
        msj2="Open"
    else:
        msj2="Closed"
    form=forms.EnquiryForm()
    if request.method=="POST":
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enquiry Submitted Successfully...")
            return HttpResponseRedirect("/")
    return render(request,"TestApp/home.html",{"form":form,"msj1":msj1,"msj2":msj2})



def feedback_view(request):
    form=forms.FeedbackForm()
    if request.method=="POST":
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thankyou For Your Valuable Feedback")
            return HttpResponseRedirect("/")
    return render(request,"TestApp/feedback.html",{"form":form})



def call_back(request):
    form=forms.RCForm()
    if request.method=="POST":
        form=forms.RCForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Will Receive A Call Back Soon.")
            return HttpResponseRedirect("/")
    return render(request,"TestApp/call.html",{"form":form})


def contact_view(request):
    return render(request,"TestApp/contact.html")



def product_view(request):
    product=Product.objects.all()
    return render(request,"TestApp/product.html",{"product":product})


def about_view(request):
    return render(request,"TestApp/about.html")

def privacy_view(request):
    return render(request,"TestApp/privacy.html")

def terms_view(request):
    return render(request,"TestApp/terms.html")


def admin_view(request):
    return render(request,"TestApp/shubham.html")
