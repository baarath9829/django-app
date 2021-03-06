from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .  import views
app_name="derma"
urlpatterns = [
    path('',views.index,name='index'),
    path('result/',views.core,name='core'),
    path('feedback/',views.feedback,name='feedback')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
