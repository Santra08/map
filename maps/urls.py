from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='maps'

urlpatterns = [
    path('first/',views.index,name='first'),
    path('download/', views.download_data, name='download_data'),
    path('download_csv/', views.download_data_csv, name='download_data_csv')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)