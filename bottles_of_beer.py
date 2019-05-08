def bottles_of_beer(bob: int):
    """Print `99 Bottles of Beer <https://en.wikipedia.org/wiki/99_Bottles_of_Beer>`

    :param bob: {int} must be an integer
    :return: {str} lyrics
    """

    if bob < 1:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        return

    tmp = bob
    bob -= 1

    print("""{} bottles of beer on the wall, {} bottles of beer.
          Take one down, pass it around, {} bottles of beer on the wall...
          """.format(tmp,
                     tmp,
                     bob))

    bottles_of_beer(bob)
