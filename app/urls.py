from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subject_data', views.SubjectDataViewSet)


urlpatterns = [
    path('', views.end_points),

    # fro the subject data router
    path('', include(router.urls)),

    path('', include('rest_framework.urls')),

    path('search_for_subject/', views.SearchForSubject.as_view()),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
