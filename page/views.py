from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def Globalcash(request):
	return render(request, 'Globalcash.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def login(request):
	return render(request, 'login.html', {})

def vip(request):
	return render(request, 'vip.html', {})

def services(request):
	return render(request, 'services.html', {})

def about(request):
	return render(request, 'about.html', {})

def logout(request):
	return render(request, 'logout.html', {})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(number, message, name, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "Globalcash.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')