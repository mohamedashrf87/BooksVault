from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("authors", views.authors, name="authors"),
    path("publishers", views.publishers, name="publishers"),
    path("lists", views.lists, name="lists"),

    path("new/book", views.new_book, name="new-book"),
    path("new/author", views.new_author, name="new-author"),
    path("new/publisher", views.new_publisher, name="new-publisher"),
    path("create/new/list", views.new_list, name="new-list"),

    path("book/<int:BookID>", views.book, name="book"),
    path("edit/book/<int:BookID>", views.edit_book, name="edit-book"),
    path("add/book/<int:BookID>/to/list", views.book, name="book"),
    path("delete/book/<int:BookID>/to/list", views.book, name="book"),

    path("author/<int:AuthorID>", views.author, name="author"),
    path("publisher/<int:PublisherID>", views.publisher, name="publisher"),
    path("list/<int:ListID>", views.list, name="list"),
    
    path("create/account", views.create_account, name="create-account"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]