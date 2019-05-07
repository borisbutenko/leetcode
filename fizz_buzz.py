def fizz_buzz(max_num: int = 100) -> list:
    """`FizzBuzz classic <https://en.wikipedia.org/wiki/Fizz_buzz>`

    :param max_num: {int} max number for FizzBuzz loop
    """

    max_num += 1
    lst = []

    for i in range(0, max_num):
        text = ""

        if i % 3 == 0:
            text += "Fizz"
        if i % 5 == 0:
            text += "Buzz"

        lst.append(text or i)  # or print(text or i)

    return lst


print(fizz_buzz())  # or fizz_buzz if not return the list
