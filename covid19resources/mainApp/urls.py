from django.urls import path
from . import views
app_name="mainApp"
urlpatterns = [
    path('',views.index,name='index'),
    path('add_new/',views.add_new,name="add_new_resource"),
    path('filter_search/',views.filter_search,name="filter_index")
]