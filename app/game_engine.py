import abc
from typing import ClassVar, Protocol

from app.game_words_processor import GameWordsProcessor


class GameEngineAsAbstract(abc.ABC):
    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError


# class GameEngine2(GameEngineAsAbstract):
#     ...


class GameEngineAsProtocol(Protocol):
    def run(self) -> None:
        raise NotImplementedError


# class GameEngine(GameEngineAsAbstract):
class GameEngine:
    _EXIT_TEXT: ClassVar[str] = '1'

    def __init__(self):
        self._game_words_processor = GameWordsProcessor()

    @property
    def _last_char(self) -> str:
        return self._game_words_processor.last_char

    def _handle_input(self) -> str:
        prompt_message = 'Введи слово.'
        if self._last_char:
            prompt_message = f'{prompt_message} Оно должно начинаться с буквы "{self._last_char}"'
        print(prompt_message)

        return input(':')

    def run(self) -> None:
        start_message = """Добро пожаловать в игру:
"Слова"

Для игры вводите слова. Слова без учёта первой буквы, если это не самое первое слово.
Для выхода нажмите [Enter] и следуйте дальнейшим инструкциям.
"""
        print(start_message)

        is_continue_game = True
        while is_continue_game:

            while True:
                # [handle_input]-[BEGIN]
                input_text = self._handle_input()
                # [handle_input]-[END]

                # [handle_exit]-[BEGIN]
                if not input_text:
                    input_for_exit: str = input(
                        f'Вы уверены что хотите выйти? '
                        f'Введите {self._EXIT_TEXT} для выхода. Или что угодно для продолжения.'
                    )
                    if input_for_exit == self._EXIT_TEXT:
                        is_continue_game = False
                        break
                # [handle_exit]-[END]

                # [handle_word]-[BEGIN]
                word: str = f'{self._last_char}{input_text}'
                try:
                    self._game_words_processor.add_next_word(word=word)
                except ValueError as exc:
                    print(exc)
                else:
                    break
                # [handle_word]-[END]

        self._goodbye()

    @staticmethod
    def _goodbye() -> None:
        print("""Благодарю вас за игру.
Всего хорошего! :)""")
