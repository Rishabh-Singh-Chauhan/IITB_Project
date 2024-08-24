from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseListView, basename='courses')
router.register(r'courses/(?P<pk>\d+)', views.CourseDetailView, basename='course')
router.register(r'instances', views.CourseInstanceListView, basename='instances')
router.register(r'instances/(?P<year>\d+)/(?P<semester>\d+)', views.CourseInstanceListView, basename='instances')
router.register(r'instances/(?P<year>\d+)/(?P<semester>\d+)/(?P<pk>\d+)', views.CourseInstanceDetailView, basename='instance')

urlpatterns = [
    path('', include(router.urls)),
]