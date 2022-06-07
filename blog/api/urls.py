from django.urls import path
from .views import PeanutList, PeanutDetail

urlpatterns = [
    path('', PeanutList.as_view()),
    path('<int:pk>/', PeanutDetail.as_view()),
]