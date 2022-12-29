from django.urls import path
from callretriver.api import views

urlpatterns = [
    path('company/', views.CompanyView.as_view()),
    path('team/', views.TeamView.as_view()),
    path('user/', views.UserView.as_view()),
    path('call/<call_id>/', views.CallView.as_view())
]
