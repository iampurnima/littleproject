from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home, name = "home"),
    path('about/',views.about, name = "about"),
    path('book/',views.book, name = "book"),
    path('menu/',views.menuPage, name = "menu"),
    path('menu_item/<int:pk>',views.display_menu_item,name="menu_item"),
    path('blog/',views.form_view,name="blog"),
]
