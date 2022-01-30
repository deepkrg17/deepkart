from django.contrib import admin
from django.urls import path
from shop import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='static/dklogo.ico')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('prodview/<str:pid>', views.prodview, name='prodview'),
    path('tracker/', views.tracker, name='tracker'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)