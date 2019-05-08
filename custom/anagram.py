def anagram(word_1: str,
            word_2: str) -> bool:
    """Anagram check example

    :param word_1: {str}
    :param word_2: {str}
    :return: {bool}
    """
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    return sorted(word_1) == sorted(word_2)
