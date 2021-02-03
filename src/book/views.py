from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_author = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_author,
    }
    return render(request, 'book/index.html', context)


class BookListView(generic.ListView):
    model = Book
    #template_name = "book_list.html"
    #context_object_name = "book_list"
    #query = Book.objects.filter(title__icontains='django')[:5]

    def get_queryset(self):
        return Book.objects.filter(title__icontains='farm')[:5]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        context['my_book_list'] = Book.objects.all()

        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book/book_detail.html"


'''
def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404('Book does not exist.')
    #book_id = get.object_or_404(Book, pk = pk)

    return render(request, 'book/book_detail.html', context={'book': book_id})
'''
