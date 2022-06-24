from . import views
from django.urls import path

urlpatterns =[ 
    path('',views.load_empinfo,name='load_empinfo'),
    path('add_empdetails',views.add_empdetails,name='add_empdetails'),
    path('showdetails',views.showdetails,name='showdetails'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_empdetails/<int:pk>',views.edit_empdetails,name='edit_empdetails'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('delete_empdetails/<int:pk>',views.delete_empdetails,name='delete_empdetails'),

]
