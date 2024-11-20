from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),  # This maps the '/food/' URL to the index view
    path('foodlist/',views.food_list,name='food_list'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('add/',views.create_item,name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
  
]
