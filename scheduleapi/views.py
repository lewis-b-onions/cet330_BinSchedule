from django.shortcuts import render, HttpResponse

# Create your views here.
# function based view or class based views

# functional based view
def home(request):
    return render(request, 'bincollections/index.html')