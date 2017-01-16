from random import choice

"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """len(word) unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_counts = {}

    phrase = phrase.rstrip()
    words = phrase.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_cost_per_type = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}

    if melon_name in melon_cost_per_type:
        melon_price = melon_cost_per_type[melon_name]
        return melon_price
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

#   Organize by dictionary for ease of matching keys and appending to value lists.
    words_by_length = {}
    word_list_sorted = []

    # Iterate through input list creating key/value pairs of the word length
    # and a list of words of that length. List of words in the value must also
    # be sorted.

    for word in words:
        letter_count = len(word)

        # If that word length already exists as a key in the dictionary
        if letter_count in words_by_length.keys():
            words_by_length[letter_count].append(word)
            # Call sort() on the value so the list of words is also sorted
            words_by_length[letter_count].sort()
        else:
            # Or create a new key: value pair with the new letter_count and word
            words_by_length[letter_count] = [word]

    # Take letter_count and the word_list_sorted values, and create a new list
    # of tuples with them. Then sort by the letter_count value.
    for letter_count, word_list in words_by_length.items():
        word_list_sorted.append((letter_count, word_list))

    word_list_sorted.sort()

    return word_list_sorted


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be"
        }

    translated_phrase = []

    phrase = phrase.rstrip()
    words = phrase.split()

    # Iterate through the words in the input phrase. If the word has a pirate
    # translation, give the translated word. Otherwise use the original word.
    for word in words:
        if word in english_to_pirate.keys():
            # Do the pirate transformation
            translated_phrase.append(english_to_pirate[word])
        else:
            # Or put the regular word back
            translated_phrase.append(word)

    # Turn the resulting list of words into a sctring with spaces between words
    return " ".join(translated_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    name_lookups = {}
    game_sequence = []

    # Creating the dictionary
    #################################################################

    # Iterate through the input list to create the dictionary
    for name in names:
        # If the last letter of the name already exists as a key in the dictionary
        if name[0] in name_lookups.keys():
            name_lookups[name[0]].append(name)
            name_lookups[name[0]].sort()
        else:
            # Or create a new key: value pair with the new letter_count and word
            name_lookups[name[0]] = [name]

    # Playing the game
    #################################################################

    # Start with the first word in the list. The first time we check by index.
    # Future loops will use the last letter as the key

    ##### This loop is currently failing some of the doc tests. It works correctly
    #  when dealing with the inital_name, and with the first iteration doing the
    #  lookup, but then starts giving inconsistent results. There has to be a way to account for the first case (where we get it via index) and subsequent cases (where we're getting it via key). I image it would be something like the elegant solution:
    #     word_counts[word] = word_counts.get(word, 0) + 1
    # If I have extra time, I will revisit it

    while True:
        initial_name = names[0]
        game_sequence.append(initial_name)
        last_letter = initial_name[-1]
        names.remove(initial_name)

        if last_letter in name_lookups.keys():
            current_name = choice(name_lookups[last_letter])
            if current_name in names:
                game_sequence.append(current_name)
                last_letter = current_name[-1]
                names.remove(current_name)
            else:
                break

        else:
            break

    return game_sequence

#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
