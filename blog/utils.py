from urllib import request
from .models import Subscribers, Comment
from django.contrib import messages


def addSubscribers(email):
    subscribe = Subscribers(email=email)
    subscribe.save()

def retrieveComment(name):
    comm = Comment(name=name)
    comm.save()
    