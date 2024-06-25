from django.urls import path
from drfapp.api import views
from drfapp.api.views import AccountList, AccountDetails, CinemaList, CinemaDetails

urlpatterns = [
    path('lists', AccountList.as_view(), name='account'),
    path('lists/<int:pk>/', AccountDetails.as_view(), name='account-details'),
    path('cinema', CinemaList.as_view(), name='cinema'),
    path('cinema/<int:pk>/', CinemaDetails.as_view(), name='cinema-details'),   
]
