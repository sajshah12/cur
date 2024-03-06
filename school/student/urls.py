from django.urls import path
from student import views





urlpatterns = [
    path('',views.add, name='add'),
    path('<int:id>/',views.delete,name='delete'),
    path('update<int:id>/',views.update, name='update'),
]
