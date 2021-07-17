
from django.urls import path

# Import views
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('register', views.userregister, name="register"),
    path('sendmessage', views.sendmessage, name="sendmessage"),
    path('requesttoadmin/', views.sendmsgtoadmin, name="sendmsgtoadmin"),
    path('shared/update/<str:username>', views.shared, name="shared"),
    path('<slug:slug>', views.dashboard, name="dashboard"),


]
