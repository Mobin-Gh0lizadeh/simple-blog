from django.urls import path,include
from .views import *


app_name = 'post'
urlpatterns = [
	path('', post_list, name = 'all_post'),
    path('?P<category_slug>[-\w]+)', post_list, name='post_list_by_category'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
	path('like/<int:post_id>/', do_like, name='like'),
]
