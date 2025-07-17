from exceptions.base import DatabaseError, ApplicationError

class UserAlreadyExistsError(DatabaseError):
    def __init__(self, username: str):
        message = f"El usuario '{username}' ya existe en la base de datos."
        super().__init__(message)


class InvalidCredentialsError(ApplicationError):
    def __init__(self):
        message = "Usuario o contraseña inválidos."
        super().__init__(message)
