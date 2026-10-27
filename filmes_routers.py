from fastapi import APIRouter

from database import SessionLocal
from models import Filme, FilmeDB

router = APIRouter()

@router.get("/filmes")
async def lista_filmes():
    """
    Essa rota mostra a lista de filmes
    """
    db = SessionLocal()
    todos_filmes = db.query(FilmeDB).all()

    return todos_filmes

@router.get("/escolher_filme/{id}")
async def escolher_filme(id: int):
    """
    rota para que o usuário escolha o filme
    """
    db = SessionLocal()
    filme_escolhido = db.query(FilmeDB).filter(FilmeDB.id == id).first()
    if filme_escolhido:
        return filme_escolhido
    
    return {"mensagem": "Filme não encontrado"}


@router.get("/filmes/genero/{genero}")
async def filtrar_generos(genero: str):
    """
    rota para ver a lista de filmes por genero
    """
    db = SessionLocal()
    genero_escolhido = db.query(FilmeDB).filter(FilmeDB.genero == genero).all()
    if genero_escolhido:
        return genero_escolhido
    
    return {"mensagem": "genero não encontrado"}


@router.post("/filmes/adicionar")
async def adicionar_filme(filme: Filme):
    """
    rota para adicionar um novo filme
    """
    if not filme.nome.strip() or not filme.genero.strip():
        return {"mensagem": "Nome e gênero do filme são obrigatórios"}
    db = SessionLocal()

    filme_existente = db.query(FilmeDB).filter(FilmeDB.id == filme.id).first()
    if filme_existente:
        return {"mensagem": "Filme com esse ID já existe"}
    
    novo_filme = FilmeDB(
        id=filme.id,
        nome=filme.nome,
        genero=filme.genero
    )
    db.add(novo_filme)
    db.commit()

    return {"mensagem": "Filme adicionado com sucesso", "filme": filme}
    

@router.put("/filmes/atualizar/{id}")
async def atualizar_filmes(id: int, filme: Filme):
    """
    rota para modificar ou atualizar um filme já existente
    """
    db = SessionLocal()
    id_do_filme = db.query(FilmeDB).filter(FilmeDB.id == id).first()
    if id_do_filme:
        id_do_filme.nome = filme.nome
        id_do_filme.genero = filme.genero
        
        db.commit()
        return {"mensagem": "Filme atualizado com sucesso", "filme": id_do_filme}
    return {"mensagem": "Filme não encontrado"}


@router.delete("/filmes/deletar/{id}")
async def deletar_filmes(id: int):
    """
    rota para deletar um filme já existente
    """
    db = SessionLocal()
    apagar_filme = db.query(FilmeDB).filter(FilmeDB.id == id).first()
    if apagar_filme:
        db.delete(apagar_filme)
        db.commit()
        return {"mensagem": "Filme removido com sucesso", "filme": apagar_filme}
    return {"mensagem": "Filme não encontrado"}

