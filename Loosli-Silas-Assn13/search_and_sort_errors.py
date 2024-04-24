# Silas Loosli
# CS1400 - MWF 9:30

from card_utility import SUITS, RANKS, get_id_from_indices

def insertion_sort(card_list):
    #### INSERTION SORT CODE ####
    #### This should sort by Rank ####
    for i in range(0, len(card_list)):
        curr_element = card_list[i]
        j = i - 1
        while j >= 0 and RANKS.index(card_list[j].get_rank()) > RANKS.index(curr_element.get_rank()):
            card_list[j + 1] = card_list[j]
            j -= 1

        card_list[j + 1] = curr_element

    print("\tInsertion Sort done")


def selection_sort(card_list):
    #### SELECTION SORT CODE ####
    #### This should sort by Suit ####
    for i in range(len(card_list) - 1):
        curr_min_index = i

        for j in range(i + 1, len(card_list)):
            if SUITS.index(card_list[curr_min_index].get_suit()) > SUITS.index(card_list[j].get_suit()):
                curr_min_index = j

        if curr_min_index != len(card_list) - i:
            card_list[i], card_list[curr_min_index] = card_list[curr_min_index], card_list[i]

    print("\tSelection Sort Done")


def linear_search(card_list, card_id):
    #### LINEAR SEARCH CODE ####
    # Indicate index value if found
    # Give proper message if not found
    for i in range(len(card_list)):
        if card_id == card_list[i].get_id():
            print("Your card is at index " + str(i + 1))
            return
    print("Your card was not found")


def binary_search(card_list, card_id):
    #### BINARY SEARCH CODE ####
    # Indicate index value if found
    # Give proper message if not found
    low = 0
    high = len(card_list) - 1
    while high > low:
        mid = (high + low) // 2
        if card_id == card_list[mid].get_id():
            print("Your card is at index " + str(mid))
            return
        elif card_id > card_list[mid].get_id():
            mid = high - 1
        else:
            mid = low + 1

    print("Your card was not found")


def bubble_sort(card_list):
    #### BUBBLE SORT CODE ####
    #### This should sort by id ####
    did_swap = True
    sort_cnt = 1

    while did_swap:
        did_swap = False

        for i in range(len(card_list) - sort_cnt):
            if card_list[i].get_id() > card_list[i + 1].get_id():
                card_list[i] = card_list[i + 1]
                card_list[i + 1] = card_list[i]
                did_swap = True

            sort_cnt += 1

    print("\tBubble Sort done")
