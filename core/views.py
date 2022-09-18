
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from core.forms import ContactForm
from core.forms import SubscriberForm

def home(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form,
        'English' : 'English'
    }
    return render(request, 'index.html',context)

def error(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, '404error.html',context)

def faq(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'faq.html',context)

def about_us(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'about_us.html',context)

def contact_information(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'contact_information.html',context)

def address_book(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'address_book.html' ,context)

def contact_us(request):
    form = ContactForm()
    form1 = SubscriberForm()
    print(request.POST)
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        form1 = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        elif form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))

    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request,'contact_us.html',context)



