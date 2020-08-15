from django.shortcuts import render, get_object_or_404
from .models import Tourprogram

# Create your views here.

def all_tourprograms(request):
    """ A view to show all tour programs, including sorting and search queries """
    
    tourprograms = Tourprogram.objects.all()

    context = {
        'tourprograms': tourprograms,
    }

    return render(request, 'tourprograms/tourprograms.html', context)


def tourprogram_detail(request, tourprogram_id):
    """ A view to show individual product details """

    tourprogram = get_object_or_404(Tourprogram, pk=tourprogram_id)

    context = {
        'tourprogram': tourprogram,
    }

    return render(request, 'tourprograms/tourprogram_detail.html', context)