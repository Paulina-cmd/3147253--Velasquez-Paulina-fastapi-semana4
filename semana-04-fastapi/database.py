from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de datos de EJEMPLO en memoria (se crea fresh cada vez)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para llenar con datos de EJEMPLO
def llenar_datos_ejemplo():
    from models import Autor, Libro
    db = SessionLocal()
    
    try:
        # Datos de EJEMPLO - Autores ficticios
        autores_ejemplo = [
            Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano"),
            Autor(nombre="Isabel Allende", nacionalidad="Chilena"),
            Autor(nombre="Mario Vargas Llosa", nacionalidad="Peruano"),
            Autor(nombre="Julio Cortázar", nacionalidad="Argentino")
        ]
        
        # Datos de EJEMPLO - Libros ficticios
        libros_ejemplo = [
            Libro(titulo="Cien años de soledad", precio=25.99, paginas=432, autor_id=1),
            Libro(titulo="El amor en los tiempos del cólera", precio=19.99, paginas=368, autor_id=1),
            Libro(titulo="La casa de los espíritus", precio=22.50, paginas=512, autor_id=2),
            Libro(titulo="Eva Luna", precio=18.75, paginas=320, autor_id=2),
            Libro(titulo="La ciudad y los perros", precio=21.99, paginas=384, autor_id=3),
            Libro(titulo="La fiesta del chivo", precio=23.50, paginas=448, autor_id=3),
            Libro(titulo="Rayuela", precio=20.25, paginas=736, autor_id=4),
            Libro(titulo="Bestiario", precio=16.99, paginas=256, autor_id=4)
        ]
        
        db.add_all(autores_ejemplo)
        db.add_all(libros_ejemplo)
        db.commit()
        print("✅ Datos de EJEMPLO insertados correctamente")
        
    except Exception as e:
        db.rollback()
        print(f"Error insertando datos de ejemplo: {e}")
    finally:
        db.close()