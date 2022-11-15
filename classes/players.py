class Player:
    def __init__(self, username):
        self.username = username
        self.users_words_used = []

    def __repr__(self):
        return f'Player(username="{self.username}", users_words_used="{self.users_words_used}")'

    def getting_number_words_used(self):
        """
        получение количества использованных слов (возвращает int)
        """
        return len(self.users_words_used)

    def adding_word_used_words(self, word):
        """
        добавление слова в использованные слова (ничего не возвращает)
        """
        self.users_words_used.append(word)

    def checking_use_given_word_before(self, word):
        """
        проверка использования данного слова до этого (возвращает bool)
        """
        if word in self.users_words_used:
            return True
        else:
            return False
