from sqlalchemy import select
from database import SessionLocal
from models import Estudiante


def crear_estudiante(nombre, correo, nota):
    with SessionLocal() as session:
        estudiante = Estudiante(
            nombre=nombre,
            correo=correo,
            nota=nota,
        )
        session.add(estudiante)
        session.commit()
        session.refresh(estudiante)
        return estudiante


def listar_estudiantes():
    with SessionLocal() as session:
        sentencia = select(Estudiante).order_by(Estudiante.id)
        return session.scalars(sentencia).all()


def buscar_por_correo(correo):
    with SessionLocal() as session:
        sentencia = select(Estudiante).where(Estudiante.correo == correo)
        return session.scalars(sentencia).first()


def actualizar_nota(correo, nueva_nota):
    with SessionLocal() as session:
        sentencia = select(Estudiante).where(Estudiante.correo == correo)
        estudiante = session.scalars(sentencia).first()
        if estudiante is None:
            return False
        estudiante.nota = nueva_nota
        session.commit()
        return True


def eliminar_estudiante(correo):
    with SessionLocal() as session:
        sentencia = select(Estudiante).where(Estudiante.correo == correo)
        estudiante = session.scalars(sentencia).first()
        if estudiante is None:
            return False
        session.delete(estudiante)
        session.commit()
        return True