from django.shortcuts import render
from .models import Treasure
"""If you want to import a specific class from your current app,
you can leave off the package and type the following:
from .module import class (or function)"""

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})
