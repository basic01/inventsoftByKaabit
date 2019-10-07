# Django
from django.contrib.auth.hashers import check_password


# Utilities
import psycopg2


# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool


# Query
from apps.usuarios.querys import execute_query



def authenticate(username=None, password=None):
    """
        Authenticate function returns a user object or None.

        It takes 2 parameters, a username and a password.
    """
    resp = execute_query(f'SELECT emp_key, email, password, first_name, last_name, area, is_superuser, is_areaadmin, is_simplemortal FROM employee WHERE email = \'{username}\'', 'one')
    column_names = resp[0]
    user_val = resp[1]
    user = {column:user_val[i] for i, column in enumerate(column_names)}
    if check_password(password, user['password']):
        return user      
    return None 

def get_user(user_id=None):
    try:
        resp = execute_query(f'SELECT emp_key, email, password, first_name, last_name, area, is_superuser, is_areaadmin, is_simplemortal FROM employee WHERE emp_key = \'{user_id}\'', 'one')
        column_names = resp[0]
        user_val = resp[1]
        user = {column:user_val[i] for i, column in enumerate(column_names)}
        return user
    except Exception as e:
        return None

def login(*args, **kwargs):
    args[0].session['user'] = kwargs['user']

"""

>>> from django.contrib.auth.hashers import make_password, check_password
>>> contra = 'edgar123' 
>>> ciph_contra = make_password(contra) 
>>> print(ciph_contra) 
pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=  
>>> contra_input = 'edgar123'
>>> did_match = check_password(contra_input, ciph_contra) 
>>> print(did_match) 
True

INSERT INTO Employee VALUES('A001','edgar@mail.com','pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=','Edgar', 'Gómez', '2019-09-23 09:46:31.22461-05', NULL, TRUE, FALSE);
INSERT INTO Employee VALUES('A002','paola@mail.com','pbkdf2_sha256$150000$k0PywcaQyaaV$v/aW088rgR4LrYXJKCgviu956N7j09bmDQz4fIBl2h0=','Paola', 'QuezadaAuu', '2019-09-23 09:46:31.22461-05', NULL, TRUE, FALSE);
//Password: employee123
INSERT INTO Employee VALUES('A003','juan@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Juan', 'López', '2019-09-23 09:46:31.22461-05', NULL, FALSE, FALSE);
"""