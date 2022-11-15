import datetime

from config import LINK_LIST_URL

from utils import load_random_word, statistics_output

from classes.players import Player
count = 0



if __name__ == '__main__':
    # получение имени пользователя
    username = input(f'Ввведите имя игрока\n-')
    # создание экземпляра класса `Player`
    players = Player(username)
    # приветствие игрока
    print(f'Привет, {players.username.capitalize ()}')
    # получение элемента класска `BasicWord`
    basic_word = load_random_word(LINK_LIST_URL)
    # описание правил игры
    print(f'Составьте {basic_word.getting_number_words_used()} слов из слова {basic_word.wofd.upper()}')
    print('Слова должны быть не короче 3 букв\n'
          'Чтобы закончить игру, угадайте все слова или напишите "стоп"\n'
          'Поехали, ваше первое слово?')

    now_beginning = datetime.datetime.now()

    # цакл получения слов и проверка их на соответствие правилам
    while players.getting_number_words_used() < basic_word.getting_number_words_used():
        user_word = input()
        if len(user_word) < 3:
            print('Cлишком короткое слово')
        elif user_word == 'stop' or user_word == 'стоп':
            break
        elif user_word not in basic_word.subwords:
            print('неверно')
        elif players.checking_use_given_word_before(user_word):
            print('уже использовано')
        else:
            print('верно')
            # добоврения слова игрока в список словаря класса `Player`
            players.adding_word_used_words(user_word)

        count += 1
    now_end = datetime.datetime.now()

    print(statistics_output(players.getting_number_words_used(), count, now_end, now_beginning))
