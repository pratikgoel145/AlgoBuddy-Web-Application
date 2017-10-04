from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
   url(r'^$', views.display,name='inside'),
   url(r'^(?P<post_id>[0-9]+)/$', views.favorite, name='fav'),
   url(r'^mark/(?P<post_id>[0-9]+)/$', views.markasread, name='mark'),
   url(r'^(?P<post_id>[0-9]+)/addcomment/$', views.add_comment, name='add'),
   url(r'^.*/$', RedirectView.as_view(url='http://127.0.0.1:8000/content/5'))
#   url(r'^.*$', views.error, name='404'),
]


