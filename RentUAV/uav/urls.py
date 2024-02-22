from django.urls import path
# importing views from views
from .views import UavCreateView, UavDeleteView, UavDetailView, UavListView, UavUpdateView



urlpatterns = [
    path('uav/create', UavCreateView.as_view(), name='uav-create'),
    path('uavs', UavListView.as_view(), name='uav-list'),
    path('uav/<int:pk>/', UavDetailView.as_view(), name='uav-detail'),
    path('uav/update/<int:pk>/', UavUpdateView.as_view(), name='uav-update'),
    path('uav/delete/<int:pk>/', UavDeleteView.as_view(), name='uav-delete'),


]