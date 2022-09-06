from typing import ClassVar


class GameWordsProcessor:
    _IGNORED_CHARACTERS: ClassVar[str] = 'ьъы'

    def __init__(self):
        self.words: list[str] = []
        self.last_char: str = ''

    @property
    def amount_of_used_words(self):
        return len(self.words)

    def add_next_word(self, word: str) -> str:
        """
        For example:
        add_next_word('map') -> 'p'
        """
        # [handle_bad_first_character]-[BEGIN]
        if (
                self.last_char
                and (current_last_character := word[0]) != self.last_char
        ):
            raise ValueError(f'Слово начинается с ошибочной буквы: {current_last_character}')
        # [handle_bad_first_character]-[END]

        # [handle_existed_words]-[BEGIN]
        if (word := word.lower()) in self.words:
            raise ValueError(f'Слово уже существует: {word}')
        # [handle_existed_words]-[END]

        # [handle_ignored_characters]-[BEGIN]
        temp_word = word
        while True:
            if not temp_word:
                raise ValueError(f'Слово не подходит из-за игнорируемых символов: {word}')

            last_char = temp_word[-1]
            if last_char not in self._IGNORED_CHARACTERS:
                break

            temp_word = temp_word[:-1]
        # [handle_ignored_characters]-[END]

        # [save_state]-[BEGIN]
        self.words.append(word)
        self.last_char = last_char
        # [save_state]-[END]

        return self.last_char
