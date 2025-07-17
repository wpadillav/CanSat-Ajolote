class ApplicationError(Exception):
    """Errores generales de la aplicación (ej. validación, lógica, permisos)."""
    def __init__(self, message: str = "Error en la aplicación."):
        self.message = message
        super().__init__(self.message)


class DatabaseError(Exception):
    """Errores relacionados con la base de datos (duplicados, fallas de conexión, etc.)."""
    def __init__(self, message: str = "Error al interactuar con la base de datos."):
        self.message = message
        super().__init__(self.message)
