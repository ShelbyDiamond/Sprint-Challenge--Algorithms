'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word: str):
    # if word is less than 2 characters, return 0 occurrences
    if len(word) < 2:
        return 0
    # if occurrence of 'th' found, grab the index, set count to 1 and recall function passing in the remaining
    # characters of word to be checked
    elif word.find('th') != -1:
        index_of_occurrence = word.find('th')
        count = 1
        # +2 because .find() finds initial index of substring and 'th' is two characters long
        return count + count_th(word[index_of_occurrence + 2:])
    # No occurrences were found
    else:
        return 0