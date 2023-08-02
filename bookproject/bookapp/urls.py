from  django.urls import path
from .import views
app_name='bookapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('book/<int:book_id>/',views.details,name='details'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete')

    ]