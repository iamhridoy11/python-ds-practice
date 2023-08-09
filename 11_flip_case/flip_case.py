def flip_case(phrase, to_swap):
    # """Flip [to_swap] case each time it appears in phrase.
    #
    #     >>> flip_case('Aaaahhh', 'a')
    #     'aAAAhhh'
    #
    #     >>> flip_case('Aaaahhh', 'A')
    #     'aAAAhhh'
    #
    #     >>> flip_case('Aaaahhh', 'h')
    #     'AaaaHHH'
    #
    # """

    a = phrase.split()
    first, *second = a
    second = "".join(second)
    print(first)

flip_case("aAAAhhh", "a")
