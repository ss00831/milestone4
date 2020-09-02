from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Tourprogram, Category

# Create your views here.


def all_tourprograms(request):
    """
    A view to show all tour programs, including sorting and search queries
    """

    tourprograms = Tourprogram.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tourprograms = tourprograms.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tourprograms = tourprograms.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tourprograms = tourprograms.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('tourprograms'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tourprograms = tourprograms.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tourprograms': tourprograms,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'tourprograms/tourprograms.html', context)


def tourprogram_detail(request, tourprogram_id):
    """ A view to show individual tourprogram details """

    tourprogram = get_object_or_404(Tourprogram, pk=tourprogram_id)

    context = {
        'tourprogram': tourprogram,
    }

    return render(request, 'tourprograms/tourprogram_detail.html', context)