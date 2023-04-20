from django.urls import path
from . import views

urlpatterns = [

    # Пути для участников торговой сети
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
    # path('board/list', views.BoardListView.as_view(), name='board_list'),
    # path('board/<int:pk>', views.BoardView.as_view(), name='board'),
]
