from .views import SignupView, IndexView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "tes"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('media/<str:filepath>/', views.download_file),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
