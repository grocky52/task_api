from . import views 

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'sprints', views.Sprintviewsets)
router.register(r'tasks', views.Taskviewset)
router.register(r'users', views.Userviewset)
