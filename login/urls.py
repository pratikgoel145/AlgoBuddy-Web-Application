from django.conf.urls import url
from . import views
from content.views import display


urlpatterns = [
    url(r'^$', views.LoginForm.as_view(), name="login"),
    url(r'^register/$', views.RegisterForm.as_view(), name='register'),
    url(r'^login/$', views.LoginForm.as_view(), name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^content/$',display, name='con')
]

