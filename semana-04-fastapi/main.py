from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importaciones CORRECTAS - SIN .py
from database import Base, engine, get_db
import models

# Crear tablas PRIMERO
Base.metadata.create_all(bind=engine)

app = FastAPI()

# AUTORES
@app.post("/autores/")
def crear_autor(nombre: str, nacionalidad: str, db: Session = Depends(get_db)):
    db_autor = models.Autor(nombre=nombre, nacionalidad=nacionalidad)
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

@app.get("/autores/")
def listar_autores(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()

@app.get("/autores/{autor_id}")
def obtener_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor

# LIBROS
@app.post("/libros/")
def crear_libro(titulo: str, precio: float, paginas: int, autor_id: int, db: Session = Depends(get_db)):
    db_libro = models.Libro(titulo=titulo, precio=precio, paginas=paginas, autor_id=autor_id)
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

@app.get("/libros/")
def listar_libros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()

@app.get("/")
def root():
    return {"message": "API de Librería funcionando"}