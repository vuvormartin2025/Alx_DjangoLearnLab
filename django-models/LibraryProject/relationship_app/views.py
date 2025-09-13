from .models import Library
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from .views import list_books

# Function-based view: show all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Register view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in user after registration
            return redirect("home")  # change "home" to your landing page
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, "relationship_app/home.html")

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# ✅ Check role helpers
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# ✅ Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# helper check
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# ✅ Admin-only view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')