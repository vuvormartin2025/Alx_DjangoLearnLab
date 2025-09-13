"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # add this line
]

from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, template_name="register"),
    path("login/", views.login_view, template_name="login"),
    path("logout/", views.logout_view, template_name="logout"),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # include app urls
]
