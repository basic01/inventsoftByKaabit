from inventsoft.connections_pool import threaded_postgreSQL_pool

def execute_query(query=None, command=None):
    if query and command:
        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            cursor.execute(query)
            if command.lower() == 'all':
                query_list = cursor.fetchall()
            elif command.lower() == 'one':
                query_list = cursor.fetchone()
            column_names = [desc[0] for desc in cursor.description]
            data = [column_names, list(query_list)]
            return data
        except Exception as e:
            return None
        finally:
            if (tcp):
                tcp.putconn(connection)
                print("Threaded PostgreSQL connection pool is closed")

    return None


def call_stored_procedure(query=None, command=None):
    if query and command:
        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            cursor.execute(query)
            if command.lower() == 'one':
                query_list = cursor.fetchone()
            # elif command.lower() == 'all':
            #     query_list = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data = [column_names, list(query_list)]
            connection.commit()
            return data
        except Exception as e:
            return None
        finally:
            if (tcp):
                tcp.putconn(connection)
                print("Threaded PostgreSQL connection pool is closed")

    return None


def call_view(query=None):
    try:
        tcp = threaded_postgreSQL_pool
        connection = tcp.getconn()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return True
    except Exception as e:
        return False
    finally:
        if (tcp):
            tcp.putconn(connection)
            print("Threaded PostgreSQL connection pool is closed")


def fetch_area_user(area_code=None, user_type=None, action=None, command=None):
    if area_code and user_type and action and command:
        regex, query = None, None
        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            if area_code == 'AA':
                if user_type == 'admin':
                    regex = 'AAA0%'
                elif user_type == 'employee':
                    regex = 'AA0%'
            elif area_code == 'AV':
                if user_type == 'admin':
                    regex = 'AAV0%'
                elif user_type == 'employee':
                    regex = 'AV0%'
            elif area_code == 'AC':
                if user_type == 'admin':
                    regex = 'AAC0'
                elif user_type == 'employee':
                    regex = 'AC0%'
            if action == 'user': 
                query = f'SELECT emp_key as key, email, password, first_name, last_name, date_joined, area, is_superuser, is_areaadmin, is_simplemortal FROM Employee WHERE emp_key LIKE \'{regex}\';'
            elif action == 'id':
                query = f'SELECT * FROM Employee WHERE emp_key LIKE \'{regex}\' ORDER BY emp_key DESC LIMIT 1;'
            cursor.execute(query)
            if command.lower() == 'all':
                query_list = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                data = [column_names, list(query_list)]
            elif command.lower() == 'one':
                query_list = cursor.fetchone()
                staff_list = list(query_list)
                column_names = [desc[0] for desc in cursor.description]
                data = {column:staff_list[i] for i, column in enumerate(column_names)}
            
            return data
        except Exception as e:
            return None
        finally:
            if (tcp):
                tcp.putconn(connection)
                print("Threaded PostgreSQL connection pool is closed")
    
    return None