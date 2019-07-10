from django.conf.urls import url 
from .views import RestaurantListView, RestaurantDetailView,\
    RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView,\
    MyPostView

urlpatterns = [
    url(r'', RestaurantListView.as_view(), name='home'),
    url(r'^create/', RestaurantCreateView.as_view(), name='create'),
    url(r'^<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),
    url(r'^<slug:slug>/update', RestaurantUpdateView.as_view(), name='update'),
    url(r'^<slug:slug>/delete', RestaurantDeleteView.as_view(), name='delete'),
    url(r'^dashboard/myposts/', MyPostView.as_view(), name='my_posts'),
]
