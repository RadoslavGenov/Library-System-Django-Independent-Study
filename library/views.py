from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import BooksForm, SearchForm, MemberRegistration, LoginForm
from .models import Books, Member


class BooksListView(ListView):
    queryset = Books.objects.all()
    paginate_by = 5
    context_object_name = 'books'
    template_name = 'library/books/booklist.html'


@user_passes_test(lambda x: x.is_superuser)
def add_books(request):
    if request.method == 'POST':
        form = BooksForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        form = BooksForm(data=request.GET)
    return render(request, 'library/books/addbook.html', {'form': form})


class BookDetail(DetailView):
    template_name = 'library/books/bookview.html'
    model = Books
    context_object_name = 'book'


def search_book(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            name = search_form.cleaned_data['book_name']
            try:
                book = Books.objects.get(name=name)
                return render(request, 'library/books/searchresult.html', {'book': book})
            except Books.DoesNotExist:
                return render(request, 'library/books/searchresult.html')
    else:
        search_form = SearchForm()
    return render(request, 'library/books/searchbook.html', {'search_form': search_form})


#def register(request):
#    if request.method == 'POST':
#        member_form = MemberRegistration(request.POST)
#        if member_form.is_valid():
#            member = member_form.save(commit=False)
#            member.set_password(member_form.cleaned_data['password'])
#            member.save()
#            return redirect('library/books/#booklist.html')
#    else:
#        member_form = MemberRegistration()
#    return render(request, 'library/books/register.html', {'member_form': member_form})
#
#
#def login(request):
#    if request.method == 'POST':
#        login_form = LoginForm(request.POST)
#        if login_form.is_valid():
#            username = login_form.cleaned_data['username']
#            password = login_form.cleaned_data['password']
#            member = Member.objects.get(username=username)
#    else:
#        login_form = LoginForm()
#    return render(request, 'library/books/login.html', {'login_form': login_form})






