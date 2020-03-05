"""seo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from  post import views
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers


app_name='post'



#router = routers.DefaultRouter()
#router.register(r'post_board',views.PostViewSet)


urlpatterns = [
url('api-auth/',include('rest_framework.urls')),
url(r'^$',views.PostViewSet.as_view(), name='post'),
url(r'^post_list/(?P<postid>\d+)/$',views.PostViewSet_detail.as_view(), name='post_detail'),
url(r'^post_list/(?P<postid>\d+)/update/$', views.PostViewSet_update.as_view(), name='post_update'),
url(r'^post_list/(?P<postid>\d+)/delete/$', views.PostViewSet_delete.as_view(), name='post_delete'),
url(r'^post_list/(?P<postid>\d+)/create/$', views.PostViewSet_create.as_view(), name='post_create'),

#url(r'^',include(router.urls)),
#url('list',views.PostViewSet.as_view()),


]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

