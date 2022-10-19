from django.urls import path
from django.views.generic import TemplateView

from todo_app.views import ListListView, ItemListView

urlpatterns = [
    path('', ListListView.as_view(), name="list-view"),
    path("list/<int:list_id>/", ItemListView.as_view(), name="item-view"),
]