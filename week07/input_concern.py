def get_input() -> int:
    """Method to get user input for the height of the Sears Tower. 
    The user is prompted to enter a positive integer or 0 to quit. 
    If the input is invalid, an error message is displayed and the 
    user is prompted again. The method returns the valid height 
    entered by the user.
    
    Returns:
    -------
    height: The valid height entered by the user, as an integer.
    """
    INPUT_MESSAGE: str = "Desired height? (must be possitive integer, or 0 to quit): "
    ERROR_MESSAGE: str = "Height must be a positive integer, or 0 to quit."
    correct: bool = False
    while not correct:
        try:
            height: int = int(input(INPUT_MESSAGE))
            correct = height >= 0
        except ValueError:
            print(ERROR_MESSAGE)
    return height
