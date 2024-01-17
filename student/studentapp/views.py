from django.shortcuts import render
from .models import Student
from django.conf import settings

# Create your views here.
def bootstrap(request):
    context = {'MEDIA_URL': settings.MEDIA_URL}
    data = Student.objects.all()
    return render(request, 'bootstrap/index.html', {'data': data, 'MEDIA_URL': settings.MEDIA_URL})


def tailwind(request):
    data = Student.objects.all()
    return render(request, 'tailwind/index.html', {'data': data})