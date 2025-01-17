from . import views
from django.urls import path, re_path, include

app_name = "ecommerce_api"

urlpatterns = [
    path("users/", views.UsersView.as_view(), name="users-view"),
    re_path("products/(?:(?P<pk>\d+)/)?$", views.ProductsView.as_view(), name="products"),
    path("products/categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("products/categories/", views.CategoryListViews.as_view(), name="category-list"),
    re_path("products/reviews/(?:(?P<pk>\d+)/)?$", views.ReviewView.as_view(), name="review"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order-detail"),
    path("orders/", views.OrdersListView.as_view(), name="order-list"),
    path("order-lines/", views.OrderLinesView.as_view(), name="order-lines"),
    path("carts/", views.CartsView.as_view(), name="carts-list"),
    path("cart-items/", views.CartItemsView.as_view(), name="cart-items"),
]
