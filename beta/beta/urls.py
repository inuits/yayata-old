from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from yata import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'timesheets', views.TimesheetViewSet, base_name='timesheet')
router.register(r'customers', views.CustomerViewSet)
router.register(r'hours', views.HourViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^oauth/', include('provider.oauth2.urls', namespace = 'oauth2')),
]
