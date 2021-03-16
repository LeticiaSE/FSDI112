# instalar Django en python
# pipenv install djando
# pipenv -- version


#python -m pipenv install djando
#python -m pipenv shell
# django-admin startproject vidflix

#cd vidflix


# python management.py startapp rental

#python -m pipenv shell
# python.management.py

#RENTAL#

#rental.apps.RentalConfig


#views

from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("Test page")

def about(request):
    return HttpResponse("Leticia Espinoza")

#urls.py
from django.urls import path
from . import views

#collection of valid router for rentals app
urlpatterns = [
    path("", views.index, name="root"),
    path("test", views,test, name="test"),
    path("home/something", views.index, name="long"),
    path("about", views.index, name=)
]



# index.html
#!Enter
#css
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<div class="container">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">VidFlix</a>
  </nav>
</div>
div class "conatainer-fluid"
    <div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <a class="btn btn-info btn-lg" href="#" role="button">Check catalog</a>
</div>
<li class="nav-item active">
        <a class="nav-link" href="/about">Home <span class="sr-only">(current)</span></a>
      </li>

h3 Welcome to: h3
h1 VidFlix h1


#script
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

