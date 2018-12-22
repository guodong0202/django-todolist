from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('edit/<forloop_counter>', views.edit, name='edit'),
    path('del/<forloop_counter>', views.delete, name='delete'),
    path('strike/<forloop_counter>', views.strike, name='strike'),
    # path('cancel/<forloop_counter>', views.cancel, name='cancel'),
]