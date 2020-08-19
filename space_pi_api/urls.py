from django.conf.urls import url 
from space_pi_api import views 
 
urlpatterns = [ 
    url(r'^api/temp_history$', views.temp_history_list),
    url(r'^api/temp_history/(?P<pk>[0-9]+)$', views.temp_history_detail)
]