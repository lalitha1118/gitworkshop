# Custom python functions

def double_number(a):

    """
    Function to double a number

    Parameters
    ----------
    a: int
        number to be doubled

    Returns
    ----------
    int
        doubled value of the given number
    """
    print(f'value before double_number(): {a}')
    y=a+a
    print(f'value after double_number(): {y}')
    return y

def square_number(a):
  
    """
    Function to square a number

    Parameters
    ----------
    a: int
        number to be squared

    Returns
    ----------
    int
        squared value of the given number
    """
    y=a*a
    print(f'value before square_number(): {a}')
    print(f'value after square_number(): {y}')
    return y