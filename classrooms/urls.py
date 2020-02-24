
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API import views as cviews
from rest_framework_simplejwt.views import (TokenObtainPairView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('classroom_list/', cviews.APIListView.as_view(), name="api-classroom-list"),
    path('classroom/<int:teacher_id>/', cviews.APIDetailView.as_view(), name="api-classroom-detail"),
    path('classcreate/', cviews.APICreateView.as_view(), name="api-classroom-create"),
    path('classroom/<int:teacher_id>/update/', cviews.APIUpdateView.as_view(), name="api-classroom-update"),
    path('classroom/<int:teacher_id>/delete/', cviews.APIDeleteView.as_view(), name="api-classroom-delete"),

    path('login/',TokenObtainPairView.as_view(),name="api-login")
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
