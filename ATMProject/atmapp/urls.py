from django.urls import include,path
from rest_framework import routers
from . import views


#router=routers.DefaultRouter()
#router.register(r'listassets',views.AssetViewSet.as_view({'get':'list'}),basename='listassets')

urlpatterns=[
    #path('',include(router.urls)),
    path('atmpin_register/',views.AtmPinView.as_view({'get':'list','post':'create'})),
    path('pin_validate/',views.pin_validate.as_view(),name='pin_validate'),
    path('deposit/',views.deposit.as_view(),name='deposit'),
    path('withdraw/',views.withdraw.as_view(),name='withdraw')
    ]
    