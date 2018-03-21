from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.main.post_detail, name='post_detail'),

    url(r'^test$', views.template.index, name='template_generate'),
]
