# Django
from django.urls import path

# Views
from apps.usuarios.views import login_user
from apps.usuarios.views import render_login
from apps.usuarios.views import table
from apps.usuarios.views import logout
from apps.usuarios.views import dashboard
from apps.usuarios.views import fetch_user
from apps.usuarios.views import stock
from apps.usuarios.views import sales
from apps.usuarios.views import purchases
from apps.usuarios.views import products
from apps.usuarios.views import fetch_products
from apps.usuarios.views import staff
from apps.usuarios.views import notifications
from apps.usuarios.views import form
from apps.usuarios.views import fetch_categories_and_providers
from apps.usuarios.views import post_product
from apps.usuarios.views import delete_product
from apps.usuarios.views import fetch_product
from apps.usuarios.views import fetch_product_stock
from apps.usuarios.views import fetch_stock_product
from apps.usuarios.views import fetch_clients
from apps.usuarios.views import fetch_sellers
from apps.usuarios.views import fetch_buyers
from apps.usuarios.views import sell_product
from apps.usuarios.views import fetch_sales
from apps.usuarios.views import fetch_purchases
from apps.usuarios.views import delete_sale
from apps.usuarios.views import delete_purchase
from apps.usuarios.views import fetch_provider
from apps.usuarios.views import buy_product
from apps.usuarios.views import fetch_stock
from apps.usuarios.views import edit_stock
from apps.usuarios.views import fetch_staff
from apps.usuarios.views import post_staff
from apps.usuarios.views import get_staff_user
from apps.usuarios.views import delete_staff
from apps.usuarios.views import fetch_notifications
from apps.usuarios.views import read_all_notifications
from apps.usuarios.views import csv_save_to_disk

from apps.usuarios.views import fetch_area_adminarea

# URLPatterns
app_name='usuarios'
urlpatterns = [
    path('', render_login, name='render_login'),
    path('login/', login_user, name='login'),
    path('get_user/', fetch_user, name='get_user'),
    path('table/', table, name='table'),
    path('form/<slug:type>/', form, name='form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('stock/', stock, name='stock'),
    path('sales/', sales, name='sales'),
    path('purchases/', purchases, name='purchases'),
    
    # Products
    path('products/', products, name='products'),
    path('fetch_products/', fetch_products, name='get_products'),
    path('staff/', staff, name='staff'),
    path('notifications/', notifications, name='notifications'),
    path('categories_and_providers/', fetch_categories_and_providers, name='fetch_categories_and_providers'),
    path('post_product/', post_product, name='post_product'),
    path('delete_product/<slug:id>/', delete_product, name='delete_product'),
    path('delete_staff/<slug:id>/', delete_staff, name='delete_staff'),
    path('fetch_product/<slug:id>/', fetch_product, name='fetch_product'),
    path('fetch_product_stock/<slug:id>/', fetch_product_stock, name='fetch_product_stock'),
    path('fetch_provider/<slug:id>/', fetch_provider, name='fetch_provider'),
    path('fetch_clients/', fetch_clients, name='fetch_clients'),
    path('fetch_sellers/', fetch_sellers, name='fetch_sellers'),
    path('fetch_buyers/', fetch_buyers, name='fetch_buyers'),
    path('sell_product/', sell_product, name='sell_product'),
    path('buy_product/', buy_product, name='buy_product'),
    path('fetch_sales/<slug:flag>/', fetch_sales, name='fetch_sales'),
    path('fetch_sales/<slug:flag>/<slug:user>/', fetch_sales, name='fetch_sales1'),
    path('fetch_purchases/<slug:flag>/', fetch_purchases, name='fetch_purchases'),
    path('fetch_purchases/<slug:flag>/<slug:user>/', fetch_purchases, name='fetch_purchases1'),
    path('fetch_stock/', fetch_stock, name='fetch_stock'),
    path('delete_sale/<slug:id>/', delete_sale, name='delete_sale'),
    path('delete_purchase/<slug:id>/', delete_purchase, name='delete_purchase'),
    path('fetch_stock_product/<slug:id>/', fetch_stock_product, name='fetch_stock_product'),
    path('edit_stock/', edit_stock, name='edit_stock'),
    path('fetch_staff/<slug:user>/', fetch_staff, name='fetch_staff'),
    path('post_staff/', post_staff, name='post_staff'),
    path('get_staff_user/<slug:id>/', get_staff_user, name='get_staff_user'),
    path('fetch_notifications/', fetch_notifications, name='fetch_notifications'),
    path('read_all_notifications/<slug:id>/', read_all_notifications, name='read_all_notifications'),
    path('csv_save_to_disk/<slug:type_csv>/', csv_save_to_disk, name='csv_save_to_disk'),
    path('fetch_area_adminarea/', fetch_area_adminarea, name='fetch_area_adminarea'),
]