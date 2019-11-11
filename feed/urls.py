from django.urls import path
from . import views

urlpatterns = [
    path("", views.highlight_index, name="highlight_index"),
    path("<int:pk>/", views.highlight_detail, name="highlight_detail"),
]
