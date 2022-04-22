def counter(input_string):
    import string
    alphabet = string.ascii_letters
    count_letters = {}
    count_letters = dict()
    for i in input_string:
        if i in alphabet:
            if i in count_letters:
                count_letters[i] += 1
            else:
                count_letters[i] = 1
    return count_letters