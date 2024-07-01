from django.shortcuts import render
from .models import Clients, Questions, Answers
from .forms import AddClientModelForm, Poll_Form, Poll_Form_answ
import datetime
import json
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication


def main_page(request):
    return render(request, "main_page.html")


def courses(request):
    return render(request, "courses.html")


def morning(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message.load)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, 'morning.html', {'form': add_client})


def lite(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, 'lite.html', {'form':add_client})


def pro(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()
    return render(request, 'pro.html', {'form':add_client})


def camp(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, 'camp.html', {'form':add_client})


def individual(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, 'individual.html', {'form':add_client})


def consultations(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        #with open(message, 'rb') as fp:
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, "consult.html", {'form': add_client})


def maintenance(request):
    if request.method == "POST":
        add_client = AddClientModelForm(request.POST, request.FILES)
        if add_client.is_valid():
            add_client.save()
        m = add_client.cleaned_data
        message = json.dumps(m)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = "The content of form from Fitness Page"
        msg['From'] = "form"
        msg['To'] = "<master777p@gmail.com>"
        s = smtplib.SMTP('127.0.0.1', port=8000)
        s.send_message(msg)
        s.quit()
    else:
        add_client = AddClientModelForm()

    return render(request, "maintenance.html", {'form': add_client})


def manual(request):
    return render(request, "manual.html")


def about_me(request):
    return render(request, "about_me.html")


def poll(request):
    questions = Questions.objects.all()
    if request.method == "POST":
        poll_form = Poll_Form(request.POST, request.FILES)
        poll_form_1 = Poll_Form_answ(request.POST, request.FILES)

        if poll_form.is_valid():
            poll_entry = Clients()
            poll_entry.name =poll_form.cleaned_data['name']
            poll_entry.email = poll_form.cleaned_data['email']
            poll_entry.telegram_account = poll_form.cleaned_data['telegram_account']

            poll_entry.save()

            poll_entry.save_m2m

            if poll_form_1.is_valid():
                poll_entry_1 = Answers()
                poll_entry_1.client = poll_entry.pk
                poll_entry_1.question = Questions.objects.get(id=id)
                poll_entry_1.answer = poll_form_1.cleaned_data['answer']
                poll_entry_1.date = datetime.datetime.now()

                poll_entry_1.save()

    else:
        poll_form = Poll_Form()
        poll_form_1 = Poll_Form_answ()

    return render(request, "poll.html", {'questions': questions, 'form': poll_form, 'form_1': poll_form_1})
