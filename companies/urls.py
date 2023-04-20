from django.urls import path
from . import views

urlpatterns = [

    # Пути для участников торговой сети
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('list/', views.CompanyListView.as_view(), name='company_list'),
    # path('board/<int:pk>', views.BoardView.as_view(), name='board'),
]
