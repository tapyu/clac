def check_is_int(input_):
    """
    check if the input parameter is integer
    """
    try:
        int(input_)
        raise Exception
    except ValueError:
        pass

def tranform2bool(input_):
    """
    transform the input parameter to boolean 
    """
    assert input_[0].lower() in ['y', 'n'], 'The input of Yes/No question should start with "y" or "n", please contact with the developer'

    if input_[0].lower() == 'y':
        return True
    elif input_[0].lower() == 'n':
        return False