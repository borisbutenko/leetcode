def count_chars(s: str) -> dict:
    """Checking the chars number in a str example

    :param s: {str}
    :return: {dict}
    """
    count_dict = {}

    for c in s:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    return count_dict
