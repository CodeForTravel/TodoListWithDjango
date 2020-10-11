from django.shortcuts import render,HttpResponse

def Profile(requist, username):
    return HttpResponse('<h1> This is the profile page! </h1>')
