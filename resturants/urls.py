from django.conf.urls import url 
from .views import RestaurantListView, RestaurantDetailView,\
    RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView,\
    MyPostView

urlpatterns = [
    url('', RestaurantListView.as_view(), name='home'),
    url('create/', RestaurantCreateView.as_view(), name='create'),
    url('<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),
    url('<slug:slug>/update', RestaurantUpdateView.as_view(), name='update'),
    url('<slug:slug>/delete', RestaurantDeleteView.as_view(), name='delete'),
    url('dashboard/myposts/', MyPostView.as_view(), name='my_posts'),
]
