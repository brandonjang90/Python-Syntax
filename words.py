def print_upper_words(words, must_start_with):
    """Take a list of words and print the list in all uppercase"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with= {"h", "y"})