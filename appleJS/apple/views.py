from django.shortcuts import render, HttpResponse

# Create your views here.
def Checking(request):
    context = {
        "karon" : "page"
    }
    return render(request, "index.html", context)
