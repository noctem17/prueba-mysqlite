RESPUESTAS
1. 
El archivo models.py. En este archivo se define la clase Estudiante que hereda de Base y especifica tanto el nombre de la tabla como sus columnas a través del mapeo mapped y mapped column.

1. 
Crear el objeto: Es simplemente instanciar la clase en la memoria RAM de Python (un objeto temporal que existe mientras corre la ejecución local).

Hacerlo persistente: Implica agregar ese objeto a la sesión de SQLAlchemy  y ejecutar una transacción session.commit() para que los datos se almacenen de forma permanente en la base de datos de la aplicación.

1. 
El metodo commit confirma y consolida los cambios pendientes ya sean inserciones, actualizaciones o eliminaciones realizados dentro de la sesión actual, escribiéndolos de manera definitiva en la base de datos.

1. 
Porque la base de datos es la última línea de defensa de la integridad de los datos. Aunque el ORM maneje la interacción mediante código, la restricción a nivel de base de datos previene duplicados o inconsistencias independientemente de si los datos se insertan desde este programa, desde otra aplicación o por un error lógico en el código.

1. 
Por modularidad y orden Cada nueva entidad tendría su propia representación en models.py y sus operaciones independientes en crud.py, evitando mezclar responsabilidades

Mantenibilidad para el codigo principal main.py y la logica de negocio no se veraan saturados por consultas complejas.

Facilidad en relaciones: El ORM permite manejar relaciones complejas como uno a muchos o muchos a muchos de forma orientada a objetos, facilitando la escalabilidad del sistema sin requerir consultas SQL manuales extensas que alargan el proceso