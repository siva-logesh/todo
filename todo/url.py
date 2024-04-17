from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='home'),
             path('todo/',views.start_up,name="home"),
             path('addtask/',views.addtask,name="addtask"),
             path('done/<int:task_id>/',views.done,name="done"),
 ]