def count_characters(string: str) -> dict:
    """Returns count of characters in a string.

    Args:
        string (str): string value.

    Returns:
        dict: pairs of character and count.
    """

    # result = {}
    # for character in set(string):
    #     result[character] = string.count(character)
    # return result
    return {character: string.count(character) for character in set(string)}


print(count_characters("adadadaqweqweadasdqeq"))
