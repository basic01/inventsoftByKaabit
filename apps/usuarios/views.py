# Django
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

# Decorators
from apps.usuarios.decorators import login_required


# Utilities
import psycopg2
import re
import os
import csv


# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool


# Auth
from apps.usuarios.authentication import authenticate, get_user, login

# Query
from apps.usuarios.querys import execute_query, call_stored_procedure, call_view, fetch_area_user


# Singleton
from apps.usuarios.singleton import config, AdminArea


# Observer
from apps.usuarios.observer import ConcreteObserver


# Views
def render_login(request):
    """
        Render login function retrieves the login html
    """
    return render(request, 'login.html')


def login_user(request):
    """
        Login user do the login functionality by getting all the data by
        the http verb POST.
        We do some validations before to avoid errors.
    """
    if request.method == 'POST':
        data = {
            'response': '', 
            'status': 400
        }
        response = JsonResponse(data)
        username = request.POST['username']
        password = request.POST['password']
        regex_email = r'[a-z0-9._%+-]+@[a-z0-9.-]+[\\.][a-z]{2,}$'
        regex_pass = r'[a-z0-9._%+-@=?¿]'
        if re.match(regex_email, username) and re.match(regex_pass, password):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
                data = {
                    'response': user, 
                    'status': 200
                }
                return JsonResponse(data)
            else:
                return response
        else:
            return response


@login_required
def fetch_user(request):
    """
    fetch_user function to retrieve te current logged in user
    """
    user = request.session['user']
    resp = get_user(user_id=f'{user["emp_key"]}')
    data = {
        'user': resp
    }
    return JsonResponse(data)


@login_required
def dashboard(request):
    """
        Dashboard function retrieves the dashboard html
    """
    return render(request, 'dashboard.html')


@login_required
def products(request):
    """
        Products function retrieves the products html
    """
    return render(request, 'products.html')


@login_required
def fetch_product(request,id):
    
    data, product, view_name = {}, [], f'{id}VIEW'

    resp = call_view(f'CREATE OR REPLACE VIEW {view_name} AS SELECT Product.product_key, Product.name, Product.description, Product.price, Product.category, Product.provider, Stock.amount FROM Product, Stock WHERE Product.product_key = \'{id}\' AND Stock.product = \'{id}\';')
    if resp:
        resp = execute_query(f'SELECT * FROM {view_name}', 'one')
        if resp:
            product_list = resp[1]
            column_names = resp[0]
            product = {column:product_list[i] for i, column in enumerate(column_names)}
            data['product'] = product
        
    return JsonResponse(data)


@login_required
def fetch_product_stock(request, id):
    data, stock = {}, []

    resp = execute_query(f'SELECT * FROM Stock WHERE product = \'{id}\';', 'one')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = {column:stock_list[i] for i, column in enumerate(column_names)}
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def fetch_provider(request, id):
    data, provider = {}, []

    resp = execute_query(f'SELECT * FROM Provider WHERE provider_key = \'{id}\';', 'one')
    if resp:
        provider_list = resp[1]
        column_names = resp[0]
        provider = {column:provider_list[i] for i, column in enumerate(column_names)}
        data['provider'] = provider

    return JsonResponse(data)


@login_required
def fetch_products(request):
    """
        fetch_products function retrieves all products in the D.B.
        and sends them to the front in JSON format
    """
    data, products = {}, []
    resp = execute_query('SELECT product_key as key, name, description, price, category, provider FROM Product ORDER BY product_key ASC;', 'all')
    if resp:
        product_list = resp[1]
        column_names = resp[0]
        products = [{column:row[i] for i, column in enumerate(column_names)} for row in product_list]
        data['products'] = products

    return JsonResponse(data)


@login_required
def post_product(request):
    data = {}
    categorias = ['BOMBON', 'CHOCOLATE', 'CARAMELO', 'GALLETA', 'GOMITA', 'PALETA', 'PAPA']
    proveedores = ['DLAROSA', 'RIKOLINO', 'WONKA', 'JOLLYRAN', 'GABI', 'MARINELA', 'GAMESA', 'CORONADO', 'SABRITAS', 'COYOTES']
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        proveedor = request.POST['proveedor']
        cantidad = request.POST['cantidad']
        accion = request.POST['accion']
        if 'id' in request.POST:
            idProduct = request.POST['id']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not categoria in categorias or not proveedor in proveedores:
            data['status'] = 400
            data['error_desc'] = 'Categoria o Proveedor incorrectos'
            return JsonResponse(data)
        elif not re.match(regex_precio, precio) or not re.match(regex_cantitdad, cantidad):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            if accion == 'NEW':
                resp = call_stored_procedure(f'SELECT addProduct(\'{nombre}\', \'{descripcion}\', {float(precio)}, \'{categoria}\', \'{proveedor}\', {int(cantidad)})', 'one')
                if resp[1]:
                    data['status'] = 200
                    ConcreteObserver().update(transmitter=request.session['user']['emp_key'], receiver='ALL', description=f"Se agrego {nombre} al inventario!", area=request.session['user']['area'])
                    return JsonResponse(data)
                else:
                    data['status'] = 400
                    return JsonResponse(data)
            elif accion == 'EDIT':
                resp = call_stored_procedure(f'SELECT editProduct(\'{idProduct}\',\'{nombre}\', \'{descripcion}\', {float(precio)}, \'{categoria}\', \'{proveedor}\', {int(cantidad)})', 'one')
                if resp[1]:
                    data['status'] = 200
                    return JsonResponse(data)
                else:
                    data['status'] = 400
                    return JsonResponse(data)


@login_required
def delete_product(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deleteProduct(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


@login_required
def fetch_clients(request):
    data, clients = {}, []

    resp = execute_query('SELECT client_key as key, name, rfc, address, email, phone FROM Client', 'all')
    if resp:
        client_list = resp[1]
        column_names = resp[0]
        clients = [{column:row[i] for i, column in enumerate(column_names)} for row in client_list]
        data['clients'] = clients

    return JsonResponse(data)


@login_required
def fetch_sellers(request):
    data, sellers = {}, []

    resp = fetch_area_user(area_code='AV', user_type='employee', action='user', command='all')
    if resp:
        sellers_list = resp[1]
        column_names = resp[0]
        sellers = [{column:row[i] for i, column in enumerate(column_names)} for row in sellers_list]
        for i in range(len(sellers)):
            sellers[i]['name'] = f'{sellers[i]["first_name"]} {sellers[i]["last_name"]}'
        data['sellers'] = sellers

    return JsonResponse(data)


@login_required
def fetch_buyers(request):
    data, buyers = {}, []

    resp = fetch_area_user(area_code='AC', user_type='employee', action='user', command='all')
    if resp:
        buyers_list = resp[1]
        column_names = resp[0]
        buyers = [{column:row[i] for i, column in enumerate(column_names)} for row in buyers_list]
        for i in range(len(buyers)):
            buyers[i]['name'] = f'{buyers[i]["first_name"]} {buyers[i]["last_name"]}'
        data['buyers'] = buyers

    return JsonResponse(data)


@login_required
def table(request):
    """
        Table function retrieves the table html
    """
    return render(request, 'table.html')

@login_required
def form(request, type):
    """
        Form function retrieves the form html
    """
    return render(request, 'form.html')


@login_required
def fetch_categories_and_providers(request):
    """
        fetch_areas function retrieves all products in the D.B.
        and sends them to the front in JSON format
    """
    data, categories, providers = {}, [], []

    resp = execute_query('SELECT category_key as key, name FROM Category', 'all')
    if resp:
        categories_list = resp[1]
        column_names = resp[0]
        categories = [{column:row[i] for i, column in enumerate(column_names)} for row in categories_list]

    resp = execute_query('SELECT provider_key as key, name FROM Provider', 'all')
    if resp:
        providers_list = resp[1]
        column_names = resp[0]
        providers = [{column:row[i] for i, column in enumerate(column_names)} for row in providers_list]

    data['categories'] = categories
    data['providers'] = providers
    return JsonResponse(data)


@login_required
def logout(request):
    response = redirect('usuarios:render_login')
    del request.session['user']
    return response

@login_required
def stock(request):
    """
        Stock function retrieves the stock html
    """
    return render(request, 'stock.html')


@login_required
def fetch_stock(request):
    data, stock = {}, []
    
    resp = execute_query('SELECT Stock.id, Stock.product, Stock.amount, Product.name as product_name FROM Stock, Product WHERE Product.product_key = Stock.product ORDER BY id ASC;', 'all')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = [{column:row[i] for i, column in enumerate(column_names)} for row in stock_list]
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def fetch_stock_product(request, id):
    data, stock = {}, []

    resp = execute_query(f'SELECT Stock.id, Stock.product, Stock.amount, Product.name as product_name FROM Stock, Product WHERE Stock.id = {int(id)} AND Product.product_key = Stock.product ORDER BY id ASC;', 'one')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = {column:stock_list[i] for i, column in enumerate(column_names)}
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def edit_stock(request):
    data = {}
    if request.method == 'POST':
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_cantitdad, cantidad):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT editStock(\'{producto}\', {int(cantidad)})', 'one')
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def sales(request):
    """
        Sales function retrieves the sales html
    """
    return render(request, 'sales.html')


@login_required
def fetch_sales(request, flag, user=None):
    data, sales = {}, []
    
    if int(flag) == 1:
        resp = execute_query('SELECT Sale.id, Sale.product, Sale.amount, Sale.client, Sale.total, Sale.seller, DATE(Sale.sale_date) as sale_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Sale, Product, Client, Employee WHERE Product.product_key = Sale.product AND Client.client_key = Sale.client AND Employee.emp_key = Sale.seller;', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales
    elif int(flag) == 2:
        resp = execute_query(f'SELECT Sale.id, Sale.product, Sale.amount, Sale.client, Sale.total, Sale.seller, DATE(Sale.sale_date) as sale_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Sale, Product, Client, Employee WHERE Sale.seller = \'{user}\' AND Product.product_key = Sale.product AND Client.client_key = Sale.client AND Employee.emp_key = Sale.seller;', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales

    return JsonResponse(data)


@login_required
def sell_product(request):
    data = {}
    if request.method == 'POST':
        product = request.POST['product']
        amount = request.POST['amount']
        total = request.POST['total']
        client = request.POST['client']
        employee = request.POST['employee']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_precio, total) or not re.match(regex_cantitdad, amount):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT sellProduct(\'{product}\', {int(amount)}, \'{client}\', {float(total)}, \'{employee}\');', 'one')
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def fetch_purchases(request, flag, user=None):
    data, purchases = {}, []

    if int(flag) == 1:
        resp = execute_query('SELECT Purchase.id, Purchase.product, Purchase.amount, Purchase.provider, Purchase.total, Purchase.buyer, DATE(Purchase.purchase_date) as purchase_date, Product.name as product_name, Provider.name as provider_name, Employee.first_name, Employee.last_name  FROM Purchase, Product, Provider, Employee WHERE Product.product_key = Purchase.product AND Provider.provider_key = Purchase.provider AND Employee.emp_key = Purchase.buyer;', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales
    elif int(flag) == 2:
        resp = execute_query(f'SELECT Purchase.id, Purchase.product, Purchase.amount, Purchase.provider, Purchase.total, Purchase.buyer, DATE(Purchase.purchase_date) as purchase_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Purchase, Product, Client, Employee WHERE Purchase.buyer = \'{user}\' AND Product.product_key = Purchase.product AND Client.client_key = Purchase.provider', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales

    return JsonResponse(data)


@login_required
def buy_product(request):
    data = {}
    if request.method == 'POST':
        product = request.POST['product']
        amount = request.POST['amount']
        total = request.POST['total']
        provider = request.POST['provider']
        employee = request.POST['employee']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_precio, total) or not re.match(regex_cantitdad, amount):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT purchaseProduct(\'{product}\', {int(amount)}, \'{provider}\', {float(total)}, \'{employee}\');', 'one')
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def delete_sale(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deleteSale(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


@login_required
def delete_purchase(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deletePurchase(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


@login_required
def purchases(request):
    """
        Purchases function retrieves the purchases html
    """
    return render(request, 'purchases.html')


@login_required
def staff(request):
    """
        Staff function retrieves the staff html
    """
    return render(request, 'staff.html')


@login_required
def fetch_staff(request, user):
    data, staff = {}, []
    
    resp = execute_query(f'SELECT emp_key, email, first_name, last_name, DATE(date_joined) as date_joined, area, is_superuser, is_areaadmin, is_simplemortal FROM Employee WHERE NOT emp_key = \'{user}\';', 'all')
    if resp:
        staff_list = resp[1]
        column_names = resp[0]
        staff = [{column:row[i] for i, column in enumerate(column_names)} for row in staff_list]
        data['staff'] = staff

    return JsonResponse(data)


@login_required
def post_staff(request):
    data = {}
    areas = ['AA', 'AV', 'AC', 'SADMI']
    tipos = ['employee', 'adminarea', 'superuser']
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        ciph_contra = make_password(contraseña)
        area = request.POST['area']
        tipo = request.POST['tipo']
        accion = request.POST['accion']
        if 'id' in request.POST:
            idStaff = request.POST['id']
        if not area in areas or not tipo in tipos:
            data['status'] = 403
            data['error_desc'] = 'Categoria o Proveedor incorrectos'
            return JsonResponse(data)
        else:
            if accion == 'NEW':
                user = {
                    'email': correo,
                    'pass': ciph_contra,
                    'first_name': nombre,
                    'last_name': apellidos,
                }
                if tipo == 'adminarea':
                    config()
                    if area == 'AA':
                        resp = AdminArea().adminAlmacen(user)
                        if resp == True:
                            data['status'] = 200
                        else:
                            data['status'] = 400
                    elif area == 'AC':
                        resp = AdminArea().adminCompras(user)                    
                        if resp == True:
                            data['status'] = 200
                        else:
                            data['status'] = 400
                    elif area == 'AV':
                        resp = AdminArea().adminVentas(user)
                        if resp == True:
                            data['status'] = 200
                        else:
                            data['status'] = 400
                else:
                    emp_id = make_employee_id(area=area, user_type=tipo)
                    if tipo == 'superuser':
                        resp = call_stored_procedure(f"SELECT addNewEployee('{emp_id}',  '{user['email']}', '{user['pass']}', '{user['first_name']}', '{user['last_name']}', 'SADMI', TRUE, FALSE, FALSE)", 'one')
                        if resp[1][0] == True:
                            data['status'] = 200
                        else:
                            data['status'] = 400 
                    else:
                        resp = call_stored_procedure(f"SELECT addNewEployee('{emp_id}',  '{user['email']}', '{user['pass']}', '{user['first_name']}', '{user['last_name']}', '{area}', FALSE, FALSE, TRUE)", 'one')
                        if resp[1][0] == True:
                            data['status'] = 200
                        else:
                            data['status'] = 400 
            elif accion == 'EDIT':
                user = {
                    'email': correo,
                    'pass': contraseña,
                    'first_name': nombre,
                    'last_name': apellidos,
                    'area': area,
                }
                temo = None
                resp = execute_query(f"SELECT * FROM Employee WHERE emp_key = '{idStaff}'", 'one')
                if resp:
                    column_names = resp[0]
                    user_list = resp[1]
                    temp = {column:user_list[i] for i, column in enumerate(column_names)}
                    temp['pass'] = temp['password']
                if temp['email'] == user['email'] and temp['first_name'] == user['first_name'] and temp['last_name'] == user['last_name'] and temp['area'] == user['area']:
                    data['status'] = 200
                    data['info'] = '( ͡° ͜ʖ ͡°)'
                else:
                    emp_id = make_employee_id(area=user['area'], user_type=tipo)
                    resp = call_stored_procedure(f"SELECT editStaff('{idStaff}', '{emp_id}', '{user['first_name']}', '{user['last_name']}', '{user['email']}', '{area}')", 'one')
                    if resp[1][0] == True:
                        data['status'] = 200
                        data['info'] = 'Empleado actualizado <br> correctamente'
                    else:
                        data['status'] = 400

            return JsonResponse(data)


@login_required
def get_staff_user(request, id):
    data, user = {}, []
    resp = execute_query(f"SELECT * FROM Employee WHERE emp_key = '{id}'", 'one')
    if resp:
        column_names = resp[0]
        user_list = resp[1]
        user = {column:user_list[i] for i, column in enumerate(column_names)}
        data['user'] = user
    
    return JsonResponse(data)


@login_required
def delete_staff(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deleteUser(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


def make_employee_id(area, user_type, action='id', command='one'):
    generated_id = None
    if user_type == 'superuser':
        emp_id = execute_query(f'SELECT * FROM Employee WHERE emp_key LIKE \'SA%\' ORDER BY emp_key DESC LIMIT 1;', 'one')
        if emp_id == None:
            generated_id = f'SA001'
        else:
            key = emp_id[1][0]
            temp = str(int(key[-3:])+1)
            if len(temp) == 1:
                generated_id = f'SA00{int(key[-3:])+1}'
            elif len(tmp) == 2:
                generated_id = f'SA0{int(key[-3:])+1}'
            elif len(temp) == 3:
                generated_id = f'SA{int(key[-3:])+1}'
    else:
        if area == 'AA':
            if user_type == 'employee':
                emp_id = fetch_area_user(area_code=area, user_type=user_type, action='id', command='one')
                if emp_id == None:
                    generated_id = f'AA001'
                else:
                    key = emp_id['emp_key']
                    temp = str(int(key[-3:])+1)
                    if len(temp) == 1:
                        generated_id = f'AA00{int(key[-3:])+1}'
                    elif len(tmp) == 2:
                        generated_id = f'AA0{int(key[-3:])+1}'
                    elif len(temp) == 3:
                        generated_id = f'AA{int(key[-3:])+1}'
        elif area == 'AC':
            if user_type == 'employee':
                emp_id = fetch_area_user(area_code=area, user_type=user_type, action='id', command='one')
                if emp_id == None:
                    generated_id = f'AC001'
                else:
                    key = emp_id['emp_key']
                    temp = str(int(key[-3:])+1)
                    if len(temp) == 1:
                        generated_id = f'AC00{int(key[-3:])+1}'
                    elif len(temp) == 2:
                        generated_id = f'AC0{int(key[-3:])+1}'
                    elif len(temp) == 3:
                        generated_id = f'AC{int(key[-3:])+1}'
        elif area == 'AV':
            if user_type == 'employee':
                emp_id = fetch_area_user(area_code=area, user_type=user_type, action='id', command='one')
                if emp_id == None:
                    generated_id = f'AV001'
                else:
                    key = emp_id['emp_key']
                    temp = str(int(key[-3:])+1)
                    if len(temp) == 1:
                        generated_id = f'AV00{int(key[-3:])+1}'
                    elif len(temp) == 2:
                        generated_id = f'AV0{int(key[-3:])+1}'
                    elif len(temp) == 3:
                        generated_id = f'AV{int(key[-3:])+1}'

    return generated_id


@login_required
def notifications(request):
    """
        Notifications function retrieves the notifications html
    """
    return render(request, 'notifications.html')


@login_required
def fetch_notifications(request):
    data, notifications, resp = {}, [], None
    if request.session['user']['is_superuser']:
        resp = execute_query(f"SELECT * FROM Notification WHERE NOT transmitter = '{request.session['user']['emp_key']}' ORDER BY notification_key DESC", 'all')
    elif request.session['user']['is_areaadmin']:
        resp = execute_query(f"SELECT * FROM Notification WHERE NOT transmitter = '{request.session['user']['emp_key']}' AND (transmitter_area = '{request.session['user']['emp_key'][1:3]}' OR receiver = 'ALL') ORDER BY notification_key DESC", 'all')
    elif request.session['user']['is_simplemortal']:
        resp = execute_query(f"SELECT * FROM Notification WHERE NOT transmitter = '{request.session['user']['emp_key']}' AND (transmitter_area = '{request.session['user']['area']}' OR receiver = 'ALL') ORDER BY notification_key DESC", 'all')
    # resp = execute_query(f"SELECT * FROM Notification WHERE receiver = 'ALL' OR ", 'all')
    lastnotemp = execute_query(f"SELECT last_notification FROM NotiEmployee WHERE employee = '{request.session['user']['emp_key']}';", 'one')
    if resp:
        column_names = resp[0]
        notifications_list = resp[1]
        if lastnotemp != None:
            notifications = [{column:row[i] for i, column in enumerate(column_names)} for row in notifications_list if int(row[0]) > int(str(lastnotemp[1][0]))]
        else:
            notifications = [{column:row[i] for i, column in enumerate(column_names)} for row in notifications_list]
        data['notifications'] = notifications
    return JsonResponse(data)


@login_required
def read_all_notifications(request, id):
    data = {}
    lastnotemp = execute_query(f"SELECT id FROM NotiEmployee WHERE employee = '{request.session['user']['emp_key']}';", 'one')
    if lastnotemp == None:
        notemp = execute_query(f"SELECT id FROM NotiEmployee ORDER BY id DESC LIMIT 1;", 'one')
        if notemp == None:
            notemp = 1
        else:
            notemp = notemp[1][0]
            notemp = int(notemp)+1
        lastnotemp = call_stored_procedure(f"SELECT addNotiEmployee({notemp}, '{id}', '{request.session['user']['emp_key']}', '{request.session['user']['area']}');", 'one')
        if lastnotemp[1]:
            data['status'] = 200
            print('primera vez')
            return JsonResponse(data)
        else:
            data['status'] = 400
            return JsonResponse(data)
    else:
        resp = call_stored_procedure(f"SELECT updateNotiEmployee({id}, '{request.session['user']['emp_key']}');", 'one')
        if resp[1]:
            data['status'] = 200
            print('update')
            return JsonResponse(data)
        else:
            data['status'] = 400
            return JsonResponse(data)


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


@login_required
def csv_save_to_disk(request, type_csv):
        data, aux_name, rows, columns_names = {}, None, None, None
        if type_csv == 'SALES':
            aux_name = f"SALES-{request.session['user']['emp_key']}"
            if request.session['user']['is_superuser'] or request.session['user']['is_areaadmin']:
                resp = execute_query('SELECT Sale.id, Sale.product, Sale.amount, Sale.client, Sale.total, Sale.seller, DATE(Sale.sale_date) as sale_date FROM Sale, Product WHERE Sale.product = Product.product_key;', 'all')
                if resp:
                    rows = resp[1]
                    column_names = resp[0]
            else:
                resp = execute_query(f"SELECT id, product, amount, client, total, seller, DATE(sale_date) as sale_date FROM Sale, Product WHERE Sale.seller = '{request.session['user']['emp_key']}' AND Sale.product = Product.product_key;;", 'all')
                if resp:
                    rows = resp[1]
                    column_names = resp[0]
            rowstmp = [{column:row[i] for i, column in enumerate(column_names)} for row in rows]

            rows = rowstmp
            columns_names = column_names
        else:
            aux_name = f"PURCHASES-{request.session['user']['emp_key']}"
            if request.session['user']['is_superuser'] or request.session['user']['is_areaadmin']:
                resp = execute_query('SELECT Purchase.id, Purchase.product, Purchase.amount, Purchase.provider, Purchase.total, Purchase.buyer, DATE(Purchase.purchase_date) as purchase_date FROM Purchase, Product WHERE Purchase.product = Product.product_key;', 'all')
                if resp:
                    rows = resp[1]
                    column_names = resp[0]
            else:
                resp = execute_query(f"SELECT id, product, amount, provider, total, buyer, DATE(purchase_date) as purchase_date FROM Purchase, Product WHERE Purchase.buyer = '{request.session['user']['emp_key']}' AND Purchase.product = Product.product_key;", 'all')
                if resp:
                    rows = resp[1]
                    column_names = resp[0]
            rowstmp = [{column:row[i] for i, column in enumerate(column_names)} for row in rows]

            rows = rowstmp
            columns_names = column_names
        down_folder = get_download_path()
        table_name = down_folder + '\\' + aux_name + '.csv'
        with open(table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=columns_names)
            writer.writeheader()
            writer.writerows(rows)
            f.close()
            data['status'] = 200
        
        return JsonResponse(data)


@login_required
def fetch_area_adminarea(request):
    data = {}
    print(request.session['user']['emp_key'][1:3])
    if request.session['user']['emp_key'][1:3] == 'AA':
        data['area'] = 'AA'
    elif request.session['user']['emp_key'][1:3] == 'AV':
        data['area'] = 'AV'
    if request.session['user']['emp_key'][1:3] == 'AC':
        data['area'] = 'AC'

    return JsonResponse(data)