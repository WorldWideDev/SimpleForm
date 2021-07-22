from django.shortcuts import render, HttpResponse
from main.forms import SampleForm
# Create your views here.
def index(request):
    context = {
        'some_form': SampleForm()
    }
    return render(request, 'index.html', context)

def do_it(request):
    # what's happening here??

    result = SampleForm(request.POST)



    if result.is_valid():
        result.save()
        return HttpResponse("SUCCESS")

    context = {
        'some_form': result
    }
    return render(request, 'index.html', context)