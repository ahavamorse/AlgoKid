'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    
    first_char = word[0]
    second_char = word[1]

    if first_char == "t" and second_char == "h":
        if len(word) > 2:
            return 1 + count_th(word[1:])
        else:
            return 1
    else:
        return count_th(word[1:])
