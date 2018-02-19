from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.models import Campus_Ambassdor
from website.forms import Campus_Ambassdor_Form
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from termcolor import colored

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'website/index.html', context_dict)

def campusambassdor(request):
    form = Campus_Ambassdor_Form()
    context_dict={}
    if request.method == 'POST':
        form = Campus_Ambassdor_Form(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            email_id = request.POST['email']
            subject = "Greetings from 67th Milestone'18"
            body1 = "Hi,\n\n"+\
                   "Greetings from Team 67th Milestone'18 and welcome to our family. \n\n" +\
                   "Thank you for applying to Campus Ambassador Internship. We are looking forward to" \
                   " work with you and will get back to you soon regarding the onset of" \
                   " the program once final applications are shortlisted.\n\n"
            body2= colored("All the best!",'red')
            body3="\n\nFor more updates, stay tuned on - \n\n"+\
                   "Website - www.67thmilestone.com \n"+\
                   "Facebook - www.facebook.com/67milestone\n"+\
                   "Instagram - www.instagram.com/67thmilestone\n"+\
                   "Twitter - www.twitter.com/67th_milestone\n"
            body=body1+body2+body3
            emailsend = EmailMessage(subject,body,to=[email_id])
            emailsend.send()
            page.save()
            return redirect(success)
        else:
            error="Already!"
            context_dict['error']=error
            print(form.errors)
            print(error)
    context_dict['form']=form
    return render(request, 'website/campusamb.html', context_dict)


def success(request):
    context_dict = {}
    return render(request, 'website/Success.html', context_dict)


def contact(request):
    context_dict = {}
    return render(request, 'website/Ourteam.html', context_dict)
