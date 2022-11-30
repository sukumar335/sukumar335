from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PhotoForm
from .recognizer import recognize
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "app/home.html", context)

@login_required
def extract_view(request, *args, **kwargs):
    my_form = PhotoForm()
    context = {
        "form": my_form,
    }
    if request.method =="GET":
        pred = ()

    if request.method == "POST":
        img = request.FILES.get('photo')
        pred, others, img_name = recognize(img)
        return HttpResponseRedirect(reverse("app:result-view", kwargs={"value": str(pred[0]), "accuracy": str(pred[1])}))
        # 

    return render(request, "app/extract.html", context)

@login_required
def result_view(request, *args, **kwargs):
    print(request.path)
    var = request.path
    l = var.split("/")
    print(l)
    value = l[2]
    accuracy = l[3]
    return render(request, "app/result.html", { "val": value, "acc": accuracy})
