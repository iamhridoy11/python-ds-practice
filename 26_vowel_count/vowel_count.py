def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # make it suitable for caseless comparisions lowercase
    phrase = phrase.casefold()

    # count the vowels
    count = {x: sum([1 for char in phrase if char == x]) for x in 'aeiou'}

    print(count)

vowel_count('HOW ARE YOU? i am great!')
