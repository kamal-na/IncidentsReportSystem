from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'incidents', views.incident)

urlpatterns = [
    path('incidents/', views.incident, name='incidents'),
    path('', views.login, name='login'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns = format_suffix_patterns(urlpatterns)