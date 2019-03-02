from django.urls import path, include

from .views import TipList, TipDetail

urlpatterns = [
    path('', TipList.as_view()),
    path('<int:pk>', TipDetail.as_view()),
    path('admin/', include('rest_framework.urls')),
]
