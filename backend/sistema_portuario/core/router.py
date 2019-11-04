from rest_framework.routers import SimpleRouter

from sistema_portuario.core import views

router = SimpleRouter()
router.register(r"grupos", views.GrupoViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"empresas", views.EmpresaViewSet)
router.register(r"tipos-carga", views.TipoCargaViewSet)
router.register(r"navios", views.NavioViewSet)
router.register(r"portos", views.PortoViewSet)
router.register(r"viagens", views.ViagemViewSet)
