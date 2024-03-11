from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import EventsView, EventDetailView, create_organization, create_event

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/events/", EventsView.as_view()),  # просмотр всех мероприятий, для сортировки и фильтрации следует
    # использовать параметры, например ?ordering=-date&date_after=2024-03-11&title=Test
    path("api/events/add", create_event),  # добавление нового мероприятия
    path("api/events/<int:pk>", EventDetailView.as_view()),  # просмотр конкретного мероприятия по ключу
    path("api/organizations/add", create_organization),  # добавление новой организации
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # получение JWT токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление JWT токена
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
