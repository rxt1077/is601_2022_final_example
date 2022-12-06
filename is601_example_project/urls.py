from django.contrib import admin
from django.urls import include, path
from example_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'baked_goods', views.BakedGoodViewSet)
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('example_app/', include('example_app.urls')), 
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls')),
    path('pos/', include('pos.urls')),
]