
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import BookForm
from .models import Book

"""
def index(request):
    book_list = Book.objects.all()
    return HttpResponse(book_list)


def products(request):
    return HttpResponse("Product page.")
"""

def index(request):
    book_list = Book.objects.all()

    paginator = Paginator(book_list, 8)
    page_number = request.GET.get('page')
    book_list = paginator.get_page(page_number)

    context = {'book_list': book_list}
    return render(request, "myapp/index.html",context)

def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, "myapp/detail.html", context)


def add_book(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        book_image = request.FILES.get("book_image")

        book = Book.objects.create(
            name=name,
            description=description,
            price=price,
            book_image=book_image
        )
        book.save()

    return render(request, "myapp/add_book.html")


def update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "myapp/edit_book.html", {'form': form})

def delete(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect('/')

    return render(request, "myapp/delete.html", {'book': book})



