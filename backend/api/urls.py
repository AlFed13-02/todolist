from django.urls import path, include

from api import views


urlpatterns = [
    path('', views.TaskList.as_view()),
    path('<int:pk>/', views.TaskDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/',
         include('rest_auth.registration.urls')),
]
