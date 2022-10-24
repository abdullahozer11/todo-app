from django.contrib.auth.views import LoginView
from django.urls import path

from todo_app.views import ListListView, ItemListView, ListAddView, ItemAddView, ItemUpdateView, ListDeleteView, \
    ItemDeleteView, SignUpView

urlpatterns = [
    path('', ListListView.as_view(), name="list-view"),
    path('list/<int:list_id>/', ItemListView.as_view(), name="item-view"),
    path('list/add/', ListAddView.as_view(), name="list-add"),
    path('list/<pk>/delete/', ListDeleteView.as_view(), name="list-delete"),
    path('list/<int:list_id>/item/add/', ItemAddView.as_view(), name="item-add"),
    path('list/<int:list_id>/item/<pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('list/<int:list_id>/item/<pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('login/', LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
