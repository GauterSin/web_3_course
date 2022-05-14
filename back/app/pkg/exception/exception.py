from .base import BaseExceptionHandler


__all__ = [
        'UnauthorizedException',
        'NotAcceptableException',
        'LockedException',
        'UnauthorizedAnonymousException',
        'GoneException',
        'TokenInvalidException',
        'FailedDependencyException',
        'FailedDataReturnMoneyException',
        'UnauthorizedAccessException'
    ]


class UnauthorizedException(BaseExceptionHandler):
    """
        User input invalid data
    """
    status_code = 401
    detail = 'Invalid password or login'


class UnauthorizedAccessException(BaseExceptionHandler):
    """
        User input invalid data
    """
    status_code = 401
    detail = 'Token expired time'


class UnauthorizedOtpException(BaseExceptionHandler):
    """
        User input invalid data
    """
    status_code = 401
    detail = 'Invalid otp'


class NotAcceptableException(BaseExceptionHandler):
    """
        Role
    """
    status_code = 406
    detail = 'Not Acceptable'


class LockedException(BaseExceptionHandler):
    """
        Role
    """
    status_code = 423
    detail = 'Locked'


class UnauthorizedAnonymousException(BaseExceptionHandler):
    status_code = 401
    detail = 'Who are you? You are not welcome here'


class GoneException(BaseExceptionHandler):
    status_code = 410
    detail = 'More 3 auth session'


class TokenInvalidException(BaseExceptionHandler):
    status_code = 498
    detail = 'Token Invalid'


class FailedDependencyException(BaseExceptionHandler):
    status_code = 424
    detail = 'Go to nahuy'


class FailedDataReturnMoneyException(BaseExceptionHandler):
    status_code = 422
    detail = 'Invalid Data'
