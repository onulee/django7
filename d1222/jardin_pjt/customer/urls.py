from django.urls import path,include
from . import views

app_name='customer'
urlpatterns = [
    # html리턴
    path('clist/', views.clist, name='clist'),
    path('clistJson/', views.clistJson, name='clistJson'),
    path('cwrite/', views.cwrite, name='cwrite'),
    path('cview/<int:bno>/', views.cview, name='cview'),
    path('cviewJson/<int:bno>/', views.cviewJson, name='cviewJson'),
    path('cdeleteJson/<int:bno>/', views.cdeleteJson, name='cdeleteJson'),
    path('cwriteJson/', views.cwriteJson, name='cwriteJson'),
    # 좋아요
    path('clikes/', views.clikes, name='clikes'),
]

