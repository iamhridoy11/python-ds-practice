def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase = list(phrase)
    phrase.reverse()
    return "".join(phrase)

result = reverse_string("awesome")
print(result)
