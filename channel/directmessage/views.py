from django.shortcuts import render
import json
from channels import Group

# Create your views here.


def index(request):
    return render(request, 'chat/index.html')

# send that user a message
def foo(user):
    if user.is_authenticated:
        Group("user-{}".format(user.id)).send({
            "text": json.dumps({
            "foo": 'bar'
        })
    })
