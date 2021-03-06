from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from products import views as products_views
from carts import views as carts_views
from orders import views as orders_views
from marketing import views as marketing_views
from accounts import views as accounts_views
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', products_views.home, name='home'),
    #url(r'^$', home, name='home'),
    url(r'^s/$', products_views.search, name='search'),
    url(r'^products/$', products_views.all, name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', products_views.single, name='single_product'),
    url(r'^cart/(?P<id>\d+)/$', carts_views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', carts_views.add_to_cart, name='add_to_cart'),
    url(r'^cart/$', carts_views.view, name='cart'),
    url(r'^checkout/$', orders_views.checkout, name='checkout'),
    url(r'^orders/$', orders_views.orders, name='user_orders'),
    url(r'^ajax/dismiss_marketing_message/$', marketing_views.dismiss_marketing_message, name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', marketing_views.email_signup, name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', accounts_views.add_user_address, name='ajax_add_user_address'),

    # url(r'^blog/', include('blog.urls')),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', accounts_views.logout_view, name='auth_logout'),
    url(r'^accounts/login/$', accounts_views.login_view, name='auth_login'),
    url(r'^accounts/register/$', accounts_views.registration_view, name='auth_register'),
    url(r'^accounts/address/add/$', accounts_views.add_user_address, name='add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', accounts_views.activation_view, name='activation_view'),
] 


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
