class CustomException(Exception):
    _messages = {}

    def get_message(self, lang=None):
        if lang is None or lang not in self._messages.keys():
            return self._messages["en_US"]
        return self._messages[lang]


class InvalidUserOrPasswordException(CustomException):

    _messages = {
        "pt_BR": "Usuário e/ou senha inválidos",
        "en_US": "Invalid user and/or password"
    }
