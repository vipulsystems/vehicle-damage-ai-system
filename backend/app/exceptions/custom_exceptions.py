class AppException(Exception):
    """Base Exception for the application"""
    def __init__(self, message="Something went wrong", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class BadRequestException(AppException):
    def __init__(self, message="Bad Request"):
        super().__init__(message, 400)


class UnauthorizedException(AppException):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, 401)


class NotFoundException(AppException):
    def __init__(self, message="Resource Not Found"):
        super().__init__(message, 404)


class DatabaseException(AppException):
    def __init__(self, message="Database Error"):
        super().__init__(message, 500)


class AIModelException(AppException):
    def __init__(self, message="AI Model Error"):
        super().__init__(message, 500)