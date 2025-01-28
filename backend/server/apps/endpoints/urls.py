from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import (
    EndpointViewSet,
    MLAlgorithmViewSet,
    MLAlgorithmStatusViewSet,
    MLRequestViewSet,
    PredictView,
    ABTestViewSet,
    StopABTestView
)

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")
router.register("abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict"),
    path("api/v1/stop_ab_test/<int:ab_test_id>", StopABTestView.as_view(), name="stop_ab")
]
