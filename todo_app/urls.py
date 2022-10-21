from django.urls import path

from todo_app.views import ListListView, ItemListView, ListAddView, ItemAddView, ItemUpdateView

urlpatterns = [
    path('', ListListView.as_view(), name="list-view"),
    path('list/<int:list_id>/', ItemListView.as_view(), name="item-view"),
    path('list/add/', ListAddView.as_view(), name="list-add"),
    path('list/<int:list_id>/item/add/', ItemAddView.as_view(), name="item-add"),
    path('list/<int:list_id>/item/<pk>/update/', ItemUpdateView.as_view(), name="item-update"),
]
