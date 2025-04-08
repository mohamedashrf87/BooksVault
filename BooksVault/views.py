import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import User, Authors, Publisher, Book, List
from .choices import CATEGORIES
from .forms import UploadFileForm
import cloudinary.uploader

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    books = Book.objects.filter(user=request.user).order_by('-added_at')

    return render(request, "index.html",{
        "CATEGORIES":CATEGORIES,
        "Books":books,
    })
    
def search(request):
    if request.method != "POST":
        return HttpResponse('This method is not allowed', status=400)

    search = request.POST.get('search', '')

    results = Book.objects.filter(
        Q(name__icontains=search) | Q(ISBN__icontains=search)
    )

    return render(request, "search.html", {
        "search":search,
        "Books": results
    })

def category(request, Category):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    CATEGORY_DICT = dict(CATEGORIES)
    category_name = CATEGORY_DICT.get(Category.upper(), "Unknown Category")

    books = Book.objects.filter(category=Category)

    return render(request, "category.html", {
        "Category":category_name,
        "Books": books
    })

def authors(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    AUTHORS  = Authors.objects.filter(user=request.user)
    return render(request, "issuers.html",{
        "authorsPage":True,
        "AUTHORS":AUTHORS,
    })
    
def publishers(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    PUBLISHERS  = Publisher.objects.filter(user=request.user)
    return render(request, "issuers.html",{
        "PUBLISHERS":PUBLISHERS,
    })

def lists(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    LISTS  = List.objects.filter(user=request.user)
    return render(request, "lists.html",{
        "LISTS":LISTS,
    })
    
def new_book(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    AUTHORS  = Authors.objects.filter(user=request.user)
    PUBLISHERS = Publisher.objects.filter(user=request.user)

    if request.method == "POST":
        # Upload image to Cloudinary
        if 'image' not in request.FILES:
            return render(request, "new-book.html", {
                "imageE": "This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS": AUTHORS,
                "PUBLISHERS": PUBLISHERS,
            })

        upload_result = cloudinary.uploader.upload(request.FILES['image'])
        
        image_url = upload_result['url']

        book_name = request.POST.get('book_name')

        if not book_name :
            return render(request, "new-book.html",{
                "nameE":"This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS":AUTHORS,
                "PUBLISHERS":PUBLISHERS,
            })
        
        ISBN = request.POST.get('ISBN')

        if not ISBN :
            return render(request, "new-book.html",{
                "ISBNE":"This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS":AUTHORS,
                "PUBLISHERS":PUBLISHERS,
            })
        
        category = request.POST.get('category')

        if not category :
            return render(request, "new-book.html",{
                "categoryE":"This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS":AUTHORS,
                "PUBLISHERS":PUBLISHERS,
            })

        authors = request.POST.get('authors')

        if not authors :
            return render(request, "new-book.html",{
                "authorsE":"This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS":AUTHORS,
                "PUBLISHERS":PUBLISHERS,
            })
        
        authors = authors.split(',')
        
        publisher_name = request.POST.get('publisher')

        if not publisher_name :
            return render(request, "new-book.html",{
                "publisherE":"This field can't be empty.",
                'CATEGORIES': CATEGORIES,
                "AUTHORS":AUTHORS,
                "PUBLISHERS":PUBLISHERS,
            })
        
        publisher = Publisher.objects.get(user=request.user, name=publisher_name)
        
        book = Book.objects.create(
            user=request.user,
            name=book_name,
            ISBN=ISBN,
            category=category,
            image_url=image_url,
            publisher=publisher,
        )

        for name in authors:
            try:
                author = Authors.objects.get(user=request.user, name=name)
                book.authors.add(author)
            except Authors.DoesNotExist:
                pass
        
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "new-book.html",{
        'CATEGORIES': CATEGORIES,
        "AUTHORS":AUTHORS,
        "PUBLISHERS":PUBLISHERS,
    })
    
@csrf_exempt
def new_author(request):
    if request.method != "POST":
        return HttpResponse('This method is not allowed', 400)
    
    data = json.loads(request.body)
    name = data.get("name", "")
    biography = data.get("biography", "")
    
    author = Authors(user=request.user ,name=name, biography=biography)
    author.save()
    
    return HttpResponse(status=204)

@csrf_exempt  
def new_publisher(request):
    if request.method != "POST":
        return HttpResponse('This method is not allowed', 400)
    
    data = json.loads(request.body)
    name = data.get("name", "")
    
    publisher = Publisher(user=request.user, name=name)
    publisher.save()
    
    return HttpResponse(status=204)
     
def new_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    if request.method == "POST":
        list_name = request.POST.get('list_name')
        new_list_obj = List(
            user=request.user,
            name=list_name
        )
        new_list_obj.save()

        books_ids = request.POST.get('books_ids').split(',')
        for id in books_ids :
            try :
                book = Book.objects.get(id=id)
                new_list_obj.books.add(book)
            except Book.DoesNotExist:
                pass
        return HttpResponseRedirect(reverse("lists"))

    books = Book.objects.filter(user=request.user).order_by('-added_at')

    return render(request, "new-list.html",{
        "Books":books,
    })
    
def book(request, BookID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        book = Book.objects.get(user=request.user, id=BookID)
    except Book.DoesNotExist:
        return HttpResponse('Book Id not found', 404)
    
    return render(request, "book.html", {"Book":book})

def edit_book(request, BookID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    try:
        book = Book.objects.get(user=request.user, id=BookID)
    except Book.DoesNotExist:
        return HttpResponse('Book Id not found', 404)

    if request.method == "POST":
        # Upload image to Cloudinary if provided
        if 'image' in request.FILES:
            upload_result = cloudinary.uploader.upload(request.FILES['image'])
            image_url = upload_result['url']
            book.image_url = image_url

        # Update basic fields
        book.name = request.POST.get('book_name')
        book.ISBN = request.POST.get('ISBN')
        book.category = request.POST.get('category')

        # Update authors
        book.authors.clear()
        authors = request.POST.get('authors', '').split(',')
        for name in authors:
            name = name.strip()
            if name:
                try:
                    author = Authors.objects.get(user=request.user, name=name)
                    book.authors.add(author)
                except Authors.DoesNotExist:
                    pass  # optionally log or notify

        # Update publisher
        publisher_name = request.POST.get('publisher')
        try:
            publisher = Publisher.objects.get(user=request.user, name=publisher_name)
            book.publisher = publisher
        except Publisher.DoesNotExist:
            pass  # optionally handle or warn

        book.save()
        return HttpResponseRedirect(reverse("index"))

    # GET method: load form with existing book data
    AUTHORS = Authors.objects.filter(user=request.user)
    PUBLISHERS = Publisher.objects.filter(user=request.user)

    return render(request, "edit-book.html", {
        "Book": book,
        "CATEGORIES": CATEGORIES,
        "AUTHORS": AUTHORS,
        "PUBLISHERS": PUBLISHERS,
    })

def author(request, AuthorID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        author  = Authors.objects.get(user=request.user, id=AuthorID)
    except Authors.DoesNotExist:
        return HttpResponse('Author Id not found', 404)
    
    books = Book.objects.filter(authors__id=AuthorID).distinct()
    return render(request, "issuer.html", {
        "Author":author,
        "Books":books,
    })
    
def publisher(request, PublisherID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        publisher  = Publisher.objects.get(user=request.user, id=PublisherID)
    except Publisher.DoesNotExist:
        return HttpResponse('Publisher Id not found', 404)
    
    books = Book.objects.filter(publisher=publisher)
    return render(request, "issuer.html", {
        "Publisher":publisher,
        "Books":books,
    })

def list(request, ListID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        list  = List.objects.get(user=request.user ,id=ListID)
    except List.DoesNotExist:
        return HttpResponse('List Id not found', 404)
    
    return render(request, "list.html", {
        "List":list,
    })

def delete_book(request, BookID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        book = Book.objects.get(user=request.user, id=BookID)
    except Book.DoesNotExist:
        return HttpResponse('Book Id not found', 404)
    book.delete()

    return HttpResponseRedirect(reverse("index"))

def delete_author(request, AuthorID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        author  = Authors.objects.get(user=request.user, id=AuthorID)
    except Authors.DoesNotExist:
        return HttpResponse('Author Id not found', 404)
    
    books = Book.objects.filter(authors=author)
    
    for book in books:
        if book.authors.count() == 1:
            book.delete()
        else:
            book.authors.remove(author)
    
    author.delete()

    return HttpResponseRedirect(reverse("index"))

def delete_publisher(request, PublisherID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        publisher  = Publisher.objects.get(user=request.user, id=PublisherID)
    except Publisher.DoesNotExist:
        return HttpResponse('Publisher Id not found', 404)
    publisher.delete()

    return HttpResponseRedirect(reverse("index"))

def delete_list(request, ListID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    try:
        list  = List.objects.get(user=request.user ,id=ListID)
    except List.DoesNotExist:
        return HttpResponse('List Id not found', 404)
    list.delete()

    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    logout(request)
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if not username:
            return render(request, "login.html", {"emailE": "This field can't be empty."})

        if not password:
            return render(request, "login.html", {"passwordE": "This field can't be empty."})
        
        if not user:
            return render(request, "login.html", {
                "emailE": "Invalid email and/or password.",
                "passwordE": "Invalid email and/or password."
            })
            
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "login.html")
    
def create_account(request):
    logout(request)
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if not username:
            return render(request, "create-account.html", {"usernameE": "This field can't be empty."})

        if User.objects.filter(username=username).exists():
            return render(request, "create-account.html", {"usernameE": "This username is unavailable."})

        if not email:
            return render(request, "create-account.html", {"emailE": "This field can't be empty."})

        if User.objects.filter(email=email).exists():
            return render(request, "create-account.html", {"emailE": "This email is already registered."})

        if not password:
            return render(request, "create-account.html", {"passwordE": "This field can't be empty."})


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "create-account.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))