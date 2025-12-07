from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def render_index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")