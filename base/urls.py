from django.urls import path
from . import views
urlpatterns = [
    path('',views.stdisplay,name="stdisplay"),
    path('create',views.stinsert,name="stinsert"),
    path('edit/<int:id>', views.stedit,name="stedit"),
    path('update/<int:id>',views.stupdate,name="stupdate"),
    path('search/<int:id>',views.search,name="search"),
    path('Delete/<int:id>',views.stdel,name="stdel")
]
