from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^login/$', views.UserLoginFormView.as_view(), name='login'),

    url(r'^register/$', views.UserRegistrationFormView.as_view(), name='register'),

    url(r'^logout/$', views.logOut, name='logout'),

    url(r'^restaurants/$', views.RestaurantListView.as_view(), name='restaurants'),

    url(r'^restaurant/(?P<id>\d+)/$', views.RestaurantView.as_view(), name='restaurant'),

    url(r'^foods/$', views.AllFoodView.as_view(), name='foods'),

    url(r'^checkout/$', views.CheckoutView.as_view(), name='checkout'),

    url(r'^addtocart/(?P<food_id>\d+)/$', views.add_to_cart, name='add_to_cart'),

    url(r'^placeorder/$', views.place_order, name='place_order'),

    url(r'^superadminlogin/$', views.SuperAdminLoginFormView.as_view(), name='superadminlogin'),

    url(r'^superadminindex/$', views.SuperAdminIndexView.as_view(), name='superadminindex'),

    url(r'^superadminneworders/$', views.SuperAdminNewOrdersView.as_view(), name='superadminneworders'),

    url(r'^superadminchartjs/$', views.SuperAdminChartJsView.as_view(), name='superadminchartjs'),
]