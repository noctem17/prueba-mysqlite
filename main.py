from database import engine
from models import Base
from crud import (
    actualizar_nota,
    crear_estudiante,
    eliminar_estudiante,
    listar_estudiantes,
)


def mostrar_estudiantes():
    for estudiante in listar_estudiantes():
        print(estudiante)


def main():
    Base.metadata.create_all(engine)

    crear_estudiante(
        "Ana",
        "ana@mail.com",
        4.5,
    )
    mostrar_estudiantes()

    actualizar_nota(
        "ana@mail.com",
        4.8,
    )
    mostrar_estudiantes()

    eliminar_estudiante("ana@mail.com")
    mostrar_estudiantes()


if __name__ == "__main__":
    main()