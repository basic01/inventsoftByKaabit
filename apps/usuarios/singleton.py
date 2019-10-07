from apps.usuarios.querys import execute_query, call_stored_procedure, call_view, fetch_area_user


ADMINS = {}
ADMINS['AA'] = None
ADMINS['AV'] = None
ADMINS['AC'] = None


def config():
    av = execute_query(f'SELECT * FROM Employee WHERE area LIKE \'AAVEN\';', 'one')
    if av != None:
        column_names = av[0]
        user_data = av[1]
        user = {column:user_data[i] for i, column in enumerate(column_names)}
        ADMINS['AV'] = user
    aa = execute_query(f'SELECT * FROM Employee WHERE area LIKE \'AAALM\';', 'one')
    if aa != None:
        column_names = aa[0]
        user_data = aa[1]
        user = {column:user_data[i] for i, column in enumerate(column_names)}
        ADMINS['AA'] = user
    ac = execute_query(f'SELECT * FROM Employee WHERE area LIKE \'AACOM\';', 'one')
    if ac != None:
        column_names = ac[0]
        user_data = ac[1]
        user = {column:user_data[i] for i, column in enumerate(column_names)}
        ADMINS['AC'] = user


class AdminArea:
    def __init__(self):
        pass

    def adminVentas(self, user=None):
        if ADMINS['AV'] == None:
            resp = call_stored_procedure(f"SELECT addNewEployee('AAV01',  '{user['email']}', '{user['pass']}', '{user['first_name']}', '{user['last_name']}', 'AAVEN', FALSE, TRUE, FALSE)", 'one')
            print(resp)
            if resp[1][0] == True:
                ADMINS['AV'] = user
                return True
            return False            
        else:
            return False
    
    def adminAlmacen(self, user=None):
        if ADMINS['AA'] == None:
            resp = call_stored_procedure(f"SELECT addNewEployee('AAA01',  '{user['email']}', '{user['pass']}', '{user['first_name']}', '{user['last_name']}', 'AAALM', FALSE, TRUE, FALSE)", 'one')
            if resp[1][0] == True:
                ADMINS['AA'] = user
                return True

        else:
            return False
    
    def adminCompras(self, user=None):
        if ADMINS['AC'] == None:
            resp = call_stored_procedure(f"SELECT addNewEployee('AAC01',  '{user['email']}', '{user['pass']}', '{user['first_name']}', '{user['last_name']}', 'AACOM', FALSE, TRUE, False)", 'one')
            if resp[1][0] == True:
                ADMINS['AC'] = user
                return True
        else:
            return False
