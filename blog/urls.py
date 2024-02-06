from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
	path('<slug:slug>', views.indexdetail, name="detail"),
	path('category/<category>/', views.categoryList, name="category"),
]
