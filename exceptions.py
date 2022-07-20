class MessageException(Exception):
    """Исключение для проблем с отправкой сообщения в чат."""

    pass


class GetAPIException(Exception):
    """Исключение для проблем доступа к API."""

    pass


class UnavailableAPIException(GetAPIException):
    """Исключение для неправильного кода доступа к API."""

    pass
