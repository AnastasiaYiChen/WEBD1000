
from django.urls import path

from . import views

# URLs
#  http://127.0.0.1:8000/admin/

# home
# http://127.0.0.1:8000/portfolio/
# Entries:
#  http://127.0.0.1:8000/portfolio/entries/
#  http://127.0.0.1:8000/portfolio/entry/1/
# categories:
#  http://127.0.0.1:8000/portfolio/categories/
#  http://127.0.0.1:8000/portfolio/category/1/

app_name = 'portfolio'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('entries/', views.EntriesView.as_view(), name='entries'),
    path('<int:pk>/entry/', views.EntryView.as_view(), name='entry'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('<int:pk>/category/', views.categoryview, name='category'),
]
