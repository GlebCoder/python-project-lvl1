#!usr/bin/env python
from random import randint


def print_game_condition():
    return print("What number is missing in the progression?")


def generate_questions(number):
    questions = []
    for item in range(1, number + 1):
        progression = ""
        d = randint(1, 10)
        n = randint(5, 10)
        a0 = randint(1, 10)
        place_for_question = randint(1, n)
        i = 1
        while i <= n:
            if i != place_for_question:
                progression += str(a0 + d * (i - 1)) + " "
            else:
                progression += ".. "
            i += 1
        questions.append(progression)
    return questions


def convert_string_to_list(text):
    '''
    Converts a progression string to a progression list
    '''
    my_list = []
    if text[1] == ' ':
        my_list.append(text[0])
        i = 1
    else:
        my_list.append(text[0] + text[1])
        i = 2
    while i <= len(text) - 2:
        if text[i] != ' ' and text[i + 1] != ' ':
            my_list.append(text[i] + text[i + 1])
        elif text[i] != ' ' and text[i + 1] == ' ' and text[i - 1] == ' ':
            my_list.append(text[i])
        i += 1
    return my_list


def find_progression_member(my_list):
    '''
    Finds a missing member in a progression list
    '''
    if my_list[0] == '..':
        d = int(my_list[2]) - int(my_list[1])
        missing_member = str(int(my_list[1]) - d)
    elif my_list[-1] == '..':
        d = int(my_list[-2]) - int(my_list[-3])
        missing_member = str(int(my_list[-2]) + d)
    else:
        i = 1
        while i <= len(my_list) - 2:
            if my_list[i] == '..':
                missing_member = str(
                    int((int(my_list[i - 1]) + int(my_list[i + 1])) / 2))
                break
            else:
                i += 1
    return missing_member


def generate_right_answers(questions):
    right_answers = []
    for item in questions:
        my_list = convert_string_to_list(item)
        result = find_progression_member(my_list)
        right_answers.append(result)
    return right_answers
