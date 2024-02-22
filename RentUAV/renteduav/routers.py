from RentUAV.renteduav.viewsets import RentedUavsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('renteduav', RentedUavsViewset)