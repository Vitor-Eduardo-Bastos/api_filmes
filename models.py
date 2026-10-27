from pydantic import BaseModel

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Filme(BaseModel):
    id: int
    nome: str
    genero: str


class FilmeDB(Base):
    __tablename__ = "filmes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    genero: Mapped[str] = mapped_column(String)