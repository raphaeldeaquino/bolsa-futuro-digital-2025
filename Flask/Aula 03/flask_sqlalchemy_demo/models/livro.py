from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func

class Livro(Base):
    __tablename__ = 'livros'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(100), nullable=False)
    isbn = Column(String(13), unique=True)
    ano_publicacao = Column(Integer)
    preco = Column(Float)
    disponivel = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"<Livro(id={self.id}, titulo='{self.titulo}', autor='{self.autor})>"
    
    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        
        Returns:
            dict: Dicionário com os dados do livro
        """
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'isbn': self.isbn,
            'ano_publicacao': self.ano_publicacao,
            'preco': self.preco,
            'disponivel': self.disponivel,
            'criado_em': self.criado_em.isoformat() if self.criado_em else None,
            'atualizado_em': self.atualizado_em.isoformat() if self.atualizado_em else None
        }