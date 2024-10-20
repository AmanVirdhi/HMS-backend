from django.urls import path
from .views import get_grievances, get_user, grievance_details, post_grievance, post_user, signup_user, user_details

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', post_user, name='post_user'),
    path('users/<int:pk>', user_details, name='user_details'),
    path('signup/', signup_user, name='signup_user'),

    # Grievance URLs
    path('grievances/', get_grievances, name='get_grievances'),
    path('grievances/create/', post_grievance, name='post_grievance'),
    path('grievances/<int:pk>/', grievance_details, name='grievance_details'),
]