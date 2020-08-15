from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tourprogram

# Create your views here.

def all_tourprograms(request):
    """ A view to show all tour programs, including sorting and search queries """
    
    tourprograms = Tourprogram.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('tourprograms'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tourprograms = tourprograms.filter(queries)

    context = {
        'tourprograms': tourprograms,
        'search_term': query,
    }

    return render(request, 'tourprograms/tourprograms.html', context)


def tourprogram_detail(request, tourprogram_id):
    """ A view to show individual tourprogram details """

    tourprogram = get_object_or_404(Tourprogram, pk=tourprogram_id)

    context = {
        'tourprogram': tourprogram,
    }

    return render(request, 'tourprograms/tourprogram_detail.html', context)