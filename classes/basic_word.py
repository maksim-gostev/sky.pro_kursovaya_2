class BasicWord:
    def __init__(self, word, subwords):
        self.wofd = word
        self.subwords = subwords

    def __repr__(self):
        return f'BasicWord(word="{self.wofd}", subwords="{self.subwords}"'

    def getting_number_words_used(self):
        """
        подсчет количества подслов (вернет int)
        """
        return len(self.subwords)

    def checking_entered_word(self, word):
        """
        проверку введенного слова в списке допустимых подслов (вернет bool)
        """
        if word in self.subwords:
            return True
        else:
            return False