from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.pdt,name='pdt'),
    path('add',views.add,name='add'),
    path('show',views.show,name='show'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('delete/<int:pk>',views.delete,name='delete'),
]