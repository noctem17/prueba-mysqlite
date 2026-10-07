from sqlalchemy import Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    nota: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return (
            f"Estudiante(id={self.id}, "
            f"nombre={self.nombre!r}, "
            f"correo={self.correo!r}, "
            f"nota={self.nota})"
        )