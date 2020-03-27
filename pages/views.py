from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
#render main page
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('logreg/profile/')
    else:
        return render(request, 'pages/index.html')
