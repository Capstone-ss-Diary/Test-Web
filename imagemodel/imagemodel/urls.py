from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("ocr.urls")),
    path('classify/', include("classification.urls")),
    path('admin/', admin.site.urls),
]
