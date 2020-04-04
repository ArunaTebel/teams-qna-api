from django.urls import path, include

from qnaapi import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/current-user', views.auth.CurrentUser.as_view(), name='current_user'),
]
