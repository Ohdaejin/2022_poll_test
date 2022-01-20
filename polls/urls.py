from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns=[
    path('',views.index, name='index'), #views안의 index파일과 연결
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]