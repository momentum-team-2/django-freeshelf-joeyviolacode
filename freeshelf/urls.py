"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('', core_views.list_books, name="list_books"),
    path('books/oldest', core_views.list_books_oldest, name='list_books_oldest'),
    path('books/title', core_views.list_books_title, name="list_books_title"),
    path('category/<slug:slug>', core_views.list_books_category, name="list_books_category"),
    path('books/show_book/<int:pk>', core_views.show_book, name="show_book"),
    path('books/mark_favorite/<int:pk>', core_views.mark_favorite, name="mark_favorite"),
    path('users/<int:pk>', core_views.show_user, name="show_user"),
    path('books/comment/<int:pk>', core_views.add_comment, name="add_comment"),
    path('books/mark_not_favorite/<int:pk>', core_views.mark_not_favorite, name="mark_not_favorite"),
    path('user/favorites', core_views.show_favorites, name="show_favorites")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
