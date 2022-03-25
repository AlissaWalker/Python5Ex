def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = value.lower().replace(' ', '')
    reversed_str = value[::-1]
    if value == reversed_str:
        return True
    else:
        return False
