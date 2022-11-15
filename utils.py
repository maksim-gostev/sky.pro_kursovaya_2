import random

import requests

from classes.basic_word import BasicWord


def load_random_word(file_url):
    """
    - получит список слов с внешнего ресурса,
    - выберет случайное слово,
    - создаст экземпляр класса `BasicWord`,
    - вернет этот экземпляр.
    """

    # список слок


    list_word = []
    # получения списка со словорями с внешнего фаила
    request = requests.get(file_url)

    json_request = request.json()
    # заполнение списка слов
    for dictionary in json_request:
        word = dictionary['word']
        list_word.append(word)
    # получение рандомного слова
    random_word = random.choice(list_word)
    # создание экземпляра класса `BasicWord`
    for dictionary in request.json():
        if random_word == dictionary['word']:
            word = dictionary['word']
            subwords = dictionary['subwords']
            basic_word = BasicWord(word, subwords)
    return basic_word


def statistics_output(len_list_player, count, end, beginning):
    time_ = end - beginning

    time_second = time_.seconds

    minute = time_second // 60

    second = time_second % 60

    return f'Игра завершена, вы угадали {len_list_player} слов!\n' \
           f'За {count} попыток.\nЗатрачено времени {minute}:{"%02d" % second} '
