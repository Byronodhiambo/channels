from django.shortcuts import render

def index(request):
    return render(request, 'directmessage/index.html')

def room(request, room_name):
    return render(request, 'directmessage/message.html', {
        'room_name': room_name
    })