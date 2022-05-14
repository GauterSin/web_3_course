from .base import BaseExceptionHandler


__all__ = [
        'UnauthorizedException',
        'UnauthorizedSignatureException',
        'UnauthorizedPassowrdCheckerException',
        'UnauthorizedMoreSessionException'
    ]


class UnauthorizedException(BaseExceptionHandler):
    """
        User input invalid data
    """
    status_code = 401
    detail = 'Invalid password or login'

class UnauthorizedPassowrdCheckerException(BaseExceptionHandler):
    status_code = 401
    detail = 'Passwords do not match'


class UnauthorizedSignatureException(BaseExceptionHandler):
    status_code = 401
    detail = 'Who are you? You are not welcome here'

class UnauthorizedMoreSessionException(BaseExceptionHandler):
    status_code = 401
    detail = 'More session'
