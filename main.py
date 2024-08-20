def reverse_char(char):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    if char in alphabets.upper():
        alphabets = alphabets.upper()

    index_of_char = alphabets.index(char)
    opposite_index = 26 - index_of_char
    opp_char = (alphabets[opposite_index -1])

    return opp_char


# print(reverse('a') == 'z')
# print(reverse('b') == 'y')
# print(reverse('c') == 'x')

print(reverse_char('a') == 'z')
print(reverse_char('A') == 'z')


def atbash(txt):
    for char in txt:
        print(char)

atbash('hello')       



    