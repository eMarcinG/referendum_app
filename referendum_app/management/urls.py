from django.urls import path
from .views import (
    IdeaListView, IdeaDetailView, IdeaCreateView,
    IdeaUpdateView, IdeaDeleteView
)

urlpatterns = [
    path('', IdeaListView.as_view(), name='idea-list'),
    path('idea/<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
    path('idea/new/', IdeaCreateView.as_view(), name='idea-create'),
    path('idea/<int:pk>/edit/', IdeaUpdateView.as_view(), name='idea-update'),
    path('idea/<int:pk>/delete/', IdeaDeleteView.as_view(), name='idea-delete'),
]