from django.urls import path
from drfapp.api import views
from drfapp.api.views import AccountList, AccountDetails

urlpatterns = [
    path('lists', AccountList.as_view(), name='account'),
    path('lists/<int:pk>/', AccountDetails.as_view(), name='account-details'),
    
    
]
