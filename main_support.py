def check_is_int(input_):
    """
    check if the input parameter is integer
    """
    try:
        int(input_)
        raise Exception('The word typed cannot be a number.')
    except ValueError:
        pass

def tranform2bool(input_):
    """
    transform the input parameter to boolean 
    """
    assert input_[0].lower() in ['y', 'n'], 'The input of Yes/No question should start with "y" or "n"'

    if input_[0].lower() == 'y':
        return True
    elif input_[0].lower() == 'n':
        return False