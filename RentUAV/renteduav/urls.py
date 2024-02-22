from django.urls import path
# importing views from views
from .views import RentedUavCreateView, RentedUavUpdateView, RentedUavListView


urlpatterns = [
    path('renteduavs/create', RentedUavCreateView.as_view(), name='renteduav-create'),
    path('renteduavs', RentedUavListView.as_view(), name='renteduav-list'),
    path('renteduavs/update/<int:pk>/', RentedUavUpdateView.as_view(), name='renteduav-update'),
]