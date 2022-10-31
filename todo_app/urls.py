from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from djangoProject1 import settings
from todo_app.views import IndexView, ItemListView, ListAddView, ItemAddView, ItemUpdateView, ListDeleteView, \
    ItemDeleteView, SignUpView, AboutView, LoginPageView, ProfileView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView, name="about"),
    path('list/add/', ListAddView.as_view(), name="list-add"),
    path('list/<pk>/', ItemListView.as_view(), name="item-view"),
    path('list/<pk>/delete/', ListDeleteView.as_view(), name="list-delete"),
    path('list/<int:list_id>/item/add/', ItemAddView.as_view(), name="item-add"),
    path('list/<int:list_id>/item/<pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('list/<int:list_id>/item/<pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<username>", ProfileView.as_view(), name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)