def centered_average(lst : list)->float:
    '''
    This function take a list.
    
    Args:
        lst (list) : list of int or float
    Returns:
        avg (float) : centered_average of list
    Raises:
        TypeError: '<' not supported between instances of 'str' and 'int'
        AnyError: If anything bad happen.
    '''
    mn = min(lst)
    mx = max(lst)
    lst.remove(mn)
    lst.remove(mx)
    for x in lst:
        if lst.count(x) >= 2 :
            lst.remove(x)
    avg = sum(lst)/len(lst)
    return avg



__author__      = "Vikas Prajapati"
__copyright__   = "Copyright 2023, CDAC-PGDBDA, Bangalore"