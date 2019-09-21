import debug_toolbar
from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('gist.urls')),
    path('', include('accounts.urls')),
    path('meals/', include('meals.urls')),
]

if config('IS_DEVELOPMENT'):
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
