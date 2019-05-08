def palindrome(word: str) -> bool:
    """Palindrome check example

    :param word: {str}
    :return: {bool} is the word palindrome
    """
    word = word.lower()
    return word[::-1] == word
