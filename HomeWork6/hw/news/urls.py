from django.urls import path
from .views import NewsList, News_oneDetail

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', News_oneDetail.as_view())
]