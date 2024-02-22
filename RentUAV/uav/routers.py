from uav.viewsets import PropertiesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('uav', PropertiesViewset)