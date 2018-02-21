from django.shortcuts import render, redirect
from django import forms
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
#
# def campusambassador(request):
#     context_dict={}
#     if request.method == 'POST':
#         email = request.POST['email']
#         phone = request.POST['phone']
#         name = request.POST['name']
#         college_name = request.POST['college_name']
#         college_address = request.POST['college_addr']
#         ca_code = request.POST['ca_code']
#         reason_ca = request.POST['textarea']
#         print(email,phone,name,college_name,college_address,ca_code,reason_ca)
#         page = Campus_Ambassdor(name=name, email=email, phone=phone, college_name=college_name,
#                                 college_address=college_address,
#                                 ca_code=ca_code, reason_ca=reason_ca)
#         page.save()
#         a = Campus_Ambassdor.objects.filter(email=email).values_list()[0]
#         if a:
#             email_id = email
#             phone = phone
#             subject = "Greetings from 67th Milestone'18"
#             body1 = "Hi,\n\n" + \
#                     "Greetings from Team 67th Milestone'18 and welcome to our family. \n\n" + \
#                     "Thank you for applying to Campus Ambassador Internship. We are looking forward to" \
#                     " work with you and will get back to you soon regarding the onset of" \
#                     " the program once final applications are shortlisted.\n\n"
#             body2 = "All the best!"
#             body3 = "\n\nFor more updates, stay tuned on - \n\n" + \
#                     "Website - www.67thmilestone.com \n" + \
#                     "Facebook - www.facebook.com/67milestone\n" + \
#                     "Instagram - www.instagram.com/67thmilestone\n" + \
#                     "Twitter - www.twitter.com/67th_milestone\n"
#             body = body1 + body2 + body3
#             emailsend = EmailMessage(subject, body, to=[email_id])
#             emailsend.send()
#             context_dict={}
#             context_dict['email']=email
#             context_dict['phone'] = phone
#             return render(request,'website/Success.html',context_dict)
#         else:
#             print("Form is not ready")
#     return render(request, 'website/campusamb.html', context_dict)


def success(request,context_dict):
    return render(request, 'website/Success.html', context_dict)


def contact(request):
    return render(request, 'website/contact.html')

def sponsor(request):
    return render(request, 'website/sponsors.html')



def campusambassador(request):
    form = Campus_Ambassdor_Form()
    context_dict={}
    if request.method == 'POST':
        form = Campus_Ambassdor_Form(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            email = request.POST['email']
            phone = request.POST['phone']
            subject = "Greetings from 67th Milestone'18"
            body1 = "Hi,\n\n"+\
                   "Greetings from Team 67th Milestone'18 and welcome to our family. \n\n" +\
                   "Thank you for applying to Campus Ambassador Internship. We are looking forward to" \
                   " work with you and will get back to you soon regarding the onset of" \
                   " the program once final applications are shortlisted.\n\n"
            body2= "All the best!"
            body3="\n\nFor more updates, stay tuned on - \n\n"+\
                   "Website - www.67thmilestone.com \n"+\
                   "Facebook - www.facebook.com/67milestone\n"+\
                   "Instagram - www.instagram.com/67thmilestone\n"+\
                   "Twitter - www.twitter.com/67th_milestone\n"
            body=body1+body2+body3
            emailsend = EmailMessage(subject,body,to=[email])
            emailsend.send()
            page.save()
            print(phone,email)
            context_dict={}
            context_dict['email']=email
            context_dict['phone']=phone
            return render(request, 'website/Success.html', context_dict)
        else:
            return render(request, 'website/error.html', context_dict)
    context_dict['form']=form
    return render(request, 'website/campusamb.html', context_dict)

def error(request):
    context_dict = {}
    return render(request, 'website/error.html', context_dict)