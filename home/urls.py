from django.urls import path

from home import views

app_name = "home"


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('signup/', views.Signup.as_view(), name="signup"),
]