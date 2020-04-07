from django.shortcuts import render, redirect
from .models import tabel
# Create your views here.
def board(request):
    items = tabel.objects.all()
    return render(request, "board.html", locals())


def quit(request):
    user = request.user
    tabel.objects.filter(name=user).update(status="quit")
    return redirect("/board")