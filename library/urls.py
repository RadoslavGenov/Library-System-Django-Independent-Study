from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login'),

    url(r'^logout/$', logout, name='logout'),

    url(r'^list$', views.BooksListView.as_view(), name='list_book'),

    url(r'^search$', views.search_book, name='search_book'),

    url(r'^(?P<pk>\d+)$', views.BookDetail.as_view(), name='detail_book'),

    url(r'^add/book$', views.add_books, name='add_book'),

]

