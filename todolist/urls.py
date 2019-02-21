from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/<thing_id>', views.edit, name='编辑'),
    path('del/<thing_id>', views.delate, name='删除'),
    path('cross/<thing_id>', views.cross, name='划掉')
]
