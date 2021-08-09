from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category as CategoryModel, Entry


# Create your views here.
class HomeView(generic.ListView):
    template_name = 'portfolio/home_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Entry.objects.all()


class EntriesView(generic.ListView):
    template_name = 'portfolio/home_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Entry.objects.all()


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'portfolio/entry_results.html'


class CategoriesView(generic.ListView):
    template_name = 'portfolio/category_index.html'
    context_object_name = 'list'

    # add a field to the queryset that is the count of entries in that category
    def get_queryset(self):
        return CategoryModel.objects.annotate(num_entries=Count('entry'))


# Function view sets up category object, and all entries of this category
def categoryview(request, pk):
    category = CategoryModel.objects.get(pk=pk)
    print("category=" + category.name)

    return render(request, 'portfolio/category_results.html',
                  {'category': category, 'entries': Entry.objects.filter(category_id=pk)})
