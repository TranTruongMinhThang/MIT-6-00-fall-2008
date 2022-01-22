import copy
word = 'kappann'
score = 0
SCRABBLE_LETTER_VALUES = {'k':1, 'a': 1, 'p':1, 'n':1}
n=7
def get_word_score(word, n):
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        score += 50
    return score
get_word_score(word, n)

SCRABBLE_LETTER_VALUES['k'] += 1

print(SCRABBLE_LETTER_VALUES)

if 'a' in SCRABBLE_LETTER_VALUES:
    print('true')
else: print('fault')

print(len(SCRABBLE_LETTER_VALUES))

for letter in SCRABBLE_LETTER_VALUES.keys():
    print(letter),

list_key = list(SCRABBLE_LETTER_VALUES)
print(list_key)

two_words = []

x = 'k'
y= 'x'
tlm = x+y
print(tlm)

list_of_five = list(SCRABBLE_LETTER_VALUES)
swap_list_list = [[]]

#tìm tất cả các kiểu sắp xếp của list
# for swap in list_of_five:
#
#     temp_lists = []
#
#     for list_stub in swap_list_list:
#
#         this_list = copy.copy(list_stub)
#
#         this_list.append(swap)
#
#         temp_lists.append(this_list)
#
#         temp_lists.append(list_stub)
#
#     swap_list_list = temp_lists
#
# print(swap_list_list)

for w in word:
    print(SCRABBLE_LETTER_VALUES.get(w,4))