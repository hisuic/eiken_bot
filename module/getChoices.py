import os
import discord
import random

from module.getData import GetWord, GetMeaning

from dotenv import load_dotenv
load_dotenv()
NUMBER_OF_WORDS = os.getenv('NUMBER_OF_WORDS')

def Shuffle(input_array):
    """
    シャッフルされた配列を返す関数

    Args:
        input_array (list): 数字が格納された配列

    Returns:
        list: シャッフルされた配列
    """
    if not isinstance(input_array, list):
        raise ValueError("Input must be a list")
    
    shuffled_array = input_array.copy()
    random.shuffle(shuffled_array)
    return shuffled_array

def ShuffleWithAnswer(input_array, answer):
    """
    シャッフルされた配列と、指定した値の新しいインデックスを返す関数

    Args:
        input_array (list): 数字が格納された配列
        answer (int): 配列内のどれかの値

    Returns:
        tuple: シャッフルされた配列, シャッフル後のanswerが格納されているインデックス
    """
    if not isinstance(input_array, list):
        raise ValueError("Input must be a list")
    if answer not in input_array:
        raise ValueError("Answer must be an element of input_array")

    shuffled_array = input_array.copy()
    random.shuffle(shuffled_array)
    answer_index = shuffled_array.index(answer)

    return shuffled_array, answer_index

def GetRandomWordFromAll():
    random_number = random.randint(1, int(NUMBER_OF_WORDS))
    return random_number

def GetFourChoicesFromAll(correct_word, mode):
    # ====================================
    # About Mode
    # Mode 1: Will return set of words
    # Mode 2: Will return set of meanings
    # ====================================

    choices_id.append(correct_word)

    for i in range(3):
        candidate = GetRandomWordFromAll()
        if candidate == correct_word:
            while(1):
                candidate = GetRandomWordFromAll()
                if candidate == correct_word:
                    candidate = GetRandomWordFromAll()
                else:
                    break
        choices_id.append(candidate)

    choices_id, answer = ShuffleWithAnswer(choices_id, choices_id[0])

    if mode == 1:
        for j in range(4):
            choices.append(GetWord(choices_id[j]))
    else if mode == 2:
        for j in range(4):
            choices.append(GetMeaning(choices_id[j]))
    else:
        print("EXPECTED ERROR: Something went wrong around GetFourChoicesFromAll() in getChoices.py")

    return choices, answer
