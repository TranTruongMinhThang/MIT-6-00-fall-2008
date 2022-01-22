# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import sys

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def new_list_fragment(fragment):
    new_list = []
    for word in wordlist:
        if len(word) >= len (fragment):
            new_list.append(word[0:len(fragment)])
    return new_list

def is_fragment_valid (fragment, wordlist):
    if fragment in new_list_fragment(fragment) and fragment not in wordlist:
        return True
    else:
        return False

def is_input_valid ():
    player_input = input('Player input letter:')
    while player_input not in string.ascii_letters or len(player_input) != 1:
        player_input = input('re-input valid letter: ')
    print('')
    return player_input




def ghost():
    print ('Welcome to Ghost!')
    print ('Player 1 goes first.')
    fragment = ''
    print ('current word fragment: ','"',fragment,'"')
    # 1st fragment
    A_in = is_input_valid ()
    fragment = fragment + A_in



    # 2nd fragment
    print ('current word fragment: ','"',fragment,'"')
    print("Player 2 's turn.")
    B_in = is_input_valid ()
    fragment = fragment + B_in
    if is_fragment_valid (fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 1 's turn.")
        A_in = is_input_valid ()
        fragment = fragment + A_in
    else:
        print('Player 2 thua')
        sys.exit()


    # 3rd fragment

    if is_fragment_valid(fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 2 's turn.")
        B_in = is_input_valid()
        fragment = fragment + B_in
    else:
        print('Player 1 thua')
        sys.exit()

    # 4th fragment


    if is_fragment_valid (fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 1 's turn.")
        A_in = is_input_valid ()
        fragment = fragment + A_in
    else:
        print('Player 2 thua')
        sys.exit()

    #5th fragment
    if is_fragment_valid(fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 2 's turn.")
        B_in = is_input_valid ()
        fragment = fragment + B_in
    else:
        print('Player 1 thua')
        sys.exit()

    #6th fragment
    if is_fragment_valid (fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 1 's turn.")
        A_in = is_input_valid ()
        fragment = fragment + A_in
    else:
        print('Player 2 thua')
        sys.exit()

    #7th fragment
    if is_fragment_valid(fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 2 's turn.")
        B_in = is_input_valid ()
        fragment = fragment + B_in
    else:
        print('Player 1 thua')
        sys.exit()

    #8th fragment
    if is_fragment_valid (fragment, wordlist) == True:
        print('current word fragment: ', '"', fragment, '"')
        print("Player 1 's turn.")
        A_in = is_input_valid ()
        fragment = fragment + A_in
    else:
        print('Player 2 thua')
        sys.exit()









    #
    # if fragment in wordlist:
    #     print('Player 2 loses because "', fragment, '"is a word.')
    #
    #
    #
    #     if word[0:4] == fragment and fragment not in wordlist:
    #         print('current word fragment: ', '"', fragment, '"')
    #
    #
    # #5th fragemnt
    # print("Player 1 's turn.")
    # A_in = input('Player 1 says letter:')
    # if A_in in string.ascii_letters and len(A_in) == 1:
    #     fragment = fragment + A_in
    # if fragment in wordlist:
    #     print('Player 1 loses because no word begin with "', fragment, '"', 'or "', fragment, '" is a word.')
    #
    # for word in wordlist:
    #     if word[:5] == fragment and fragment not in wordlist:
    #         print('current word fragment: ', '"', fragment, '"')
    #
    # #6th fragemnt
    # print("Player 2 's turn.")
    # B_in = input('Player 1 says letter:')
    # if B_in in string.ascii_letters and len(B_in) == 1:
    #     fragment = fragment + B_in
    # if fragment in wordlist:
    #     print('Player 2 loses because no word begin with "', fragment, '"', 'or "', fragment, '" is a word.')
    #
    # for word in wordlist:
    #     if word[:4] == fragment and fragment not in wordlist:
    #         print('current word fragment: ', '"', fragment, '"')
    #     else:
    #         print('Player 2 loses because no word begin with "',fragment,'"','or "',fragment,'" is a word.')


ghost()
# is_input_valid()




# is_input_valid ()

# if '2' not in string.ascii_letters:
#     print('true')
# else: print('False')
