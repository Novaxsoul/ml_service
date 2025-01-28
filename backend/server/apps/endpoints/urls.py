from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import (
    EndpointViewSet,
    MLAlgorithmViewSet,
    MLAlgorithmStatusViewSet,
    MLRequestViewSet,
    PredictView
)

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict")
]
