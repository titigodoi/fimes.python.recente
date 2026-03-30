from db import db

class Filme(db.Model):
    __tablename__ = 'filmes'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    diretor = db.Column(db.String(100), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'duracao': self.duracao,
            'ano': self.ano,
            'diretor': self.diretor
        }