from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'fotografos', views.FotografoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'servicos', views.ServicoViewSet)
router.register(r'tipos-parentesco', views.TipoParentescoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]