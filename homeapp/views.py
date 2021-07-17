from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Message, Userprofile, Activitylog

from ipware import get_client_ip

import requests
import json
# Create your views here.


def index(request):
    ip, is_routable = get_client_ip(request)

    if ip is None:
        ip = "0.0.0.0"

    res = requests.get('http://ip-api.com/json/27.147.191.134')
    res2 = res.text
    new = json.loads(res2)
    print(new['regionName'])
    print(new['city'])
    return render(request, 'index.html', context={})


def dashboard(request, slug):

    if request.user is not None:
        if request.user.username == slug:
            inbox = Message.objects.filter(
                user_id=request.user.id).order_by('-created_at')
            info = request.user_agent
            activity = Activitylog()
            activity.user = request.user
            activity.activity = request.user.username + " logged in profile " + " OS: " + info.os.family + " osV: " + \
                info.os.version_string + " browser: " + info.browser.family + " browserV: " + \
                info.browser.version_string + " Device: " + info.get_device()
            activity.save()
            context = {
                'inbox': inbox,

            }
            return render(request, 'profile.html', context)
        else:
            try:
                user = User.objects.get(username=slug)
                context = {
                    'user': user

                }
                return render(request, 'sendmessage.html', context)
            except:
                context = {}
                return render(request, 'error.html', context)

    else:
        try:
            user = User.objects.get(username=slug)
            context = {
                'user': user
            }
            return render(request, 'sendmessage.html', context)
        except:
            context = {}
            return render(request, 'error.html', context)


def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard', slug=request.user.username)
        else:
            messages.warning(request, 'Invalid Credentials')

            return render(request, 'login.html', context={})
    if request.user.is_authenticated:
        return redirect('dashboard', slug=request.user.username)

    return render(request, 'login.html', context={})


def userregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.warning(
                request, "Username Exist. Please Choose Unique name")
            return redirect('register')
        user = User.objects.create_user(
            username, 'rakinbogra1828@gmail.com', password)
        authuser = authenticate(username=username, password=password)
        login(request, authuser)

        current_user = request.user

        info = request.user_agent

        data = Userprofile()
        data.user = current_user

        data.userdevice = info.get_device()
        data.useros = info.os.family
        data.userosversion = info.os.version_string

        data.userbrowser = info.browser.family
        data.userbrowserversion = info.browser.version_string
        data.save()

        # Set the acitvity
        activity = Activitylog()
        activity.user = request.user.username
        activity.activity = "Registered: name: " + request.user.username + " OS: " + info.os.family + " osV: " + \
            info.os.version_string + " browser: " + info.browser.family + " browserV: " + \
            info.browser.version_string + " Device: " + info.get_device()
        try:
            activity.reflink = request.META.get('HTTP_REFERER')
        except:
            activity.reflink = "not found"

        activity.save()

        return redirect('dashboard', slug=username)
    if request.user.is_authenticated:
        return redirect('dashboard', slug=request.user.username)

    return render(request, 'register.html', context={})


def sendmessage(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        userid = request.POST.get('userid')
        # prev = request.META.get('HTTP_REFERER')
        user = User.objects.get(pk=userid)

        info = request.user_agent

        setmessage = Message()
        setmessage.user = user
        setmessage.message = message
        setmessage.senderdevice = info.get_device()
        setmessage.senderos = info.os.family
        setmessage.senderosversion = info.os.version_string

        setmessage.senderbrowser = info.browser.family
        setmessage.senderbrowserversion = info.browser.version_string
        setmessage.save()

        activity = Activitylog()
        if request.user.is_authenticated:
            activity.user = request.user.username
        activity.activity = "Sent message: to: " + user.username + "  Sender OS: " + info.os.family + " osV: " + \
            info.os.version_string + " browser: " + info.browser.family + " browserV: " + \
            info.browser.version_string + " Device: " + info.get_device()
        activity.message = message
        activity.reflink = request.META.get('HTTP_REFERER')
        print(activity.activity)
        activity.save()

        messages.success(request, "Your messsage is sent Successfully")
        return redirect('register')


def shared(request, username):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.username == username:
                activity = Activitylog()
                activity.user = request.user.username
                activity.activity = request.user.username + " Shared profile "
                activity.message = request.user.username + " Shared profile "
                activity.save()
                return JsonResponse({"success": "success"})
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('login')


def sendmsgtoadmin(request):
    if request.method == 'POST':
        email = request.POST['email']
        adminmsg = request.POST['adminmsg']
        activity = Activitylog()
        activity.user = request.user.username
        activity.activity = "REQUEST TO ADMIN FROM " + email
        activity.message = adminmsg
        activity.save()
        return JsonResponse({'text': 'Sent to Admin'})
    else:
        return redirect('login')


def userlogout(request):
    if request.user is None:
        return redirect('home')
    logout(request)

    return redirect('login')
