from django.urls import path
from .views import ClientCreate, ClientDetail, ClientList, ClientUpdate,ClientDelete, RecepLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
      path('login/', RecepLoginView.as_view(), name='login'),
      path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
      path('', ClientList.as_view(), name='clients'),
      path('client/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
      path('create/', ClientCreate.as_view(), name='client-create'),
      path('update/<int:pk>/', ClientUpdate.as_view(), name='client-update'),
      path('delete/<int:pk>/', ClientDelete.as_view(), name='client-delete'),



      
]