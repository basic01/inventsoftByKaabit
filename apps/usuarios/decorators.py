# Django
from django.shortcuts import redirect


def login_required(func):
    """
        Login required function takes a function as a parameter.
        This function is the one we want evaluate.
    """
    # def wrapper(*args):
    def wrapper(*args, **kwargs):
        """
            Wrapper function is a must in decorators. This function does all
            the work, so we have to write TODO code implementation here.

            *args -> unnamed arguments passed in de function, avoid us to know
                     every param for differet functions.
        """
        if 'user' in args[0].session:
            return func(*args, **kwargs)
        else:
            return redirect('usuarios:render_login')

    return wrapper


