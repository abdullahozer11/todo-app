from django.contrib.auth.decorators import login_required
from django.urls import path

from todo_app.views import IndexView, ItemListView, ListAddView, ItemAddView, ItemUpdateView, ListDeleteView, \
    ItemDeleteView, SignUpView, AboutView, LoginPageView, ProfileView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView, name="about"),
    path('list/<int:list_id>/', ItemListView.as_view(), name="item-view"),
    path('list/add/', ListAddView.as_view(), name="list-add"),
    path('list/<pk>/delete/', ListDeleteView.as_view(), name="list-delete"),
    path('list/<int:list_id>/item/add/', ItemAddView.as_view(), name="item-add"),
    path('list/<int:list_id>/item/<pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('list/<int:list_id>/item/<pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('logout/', LogoutView, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView, name="profile"),
]
