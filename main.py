from sqlalchemy import create_engine,Column, String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base

db = create_engine("sqlite:///storeje.db")
Session = sessionmaker(bind=db)
session=Session()


Base = declarative_base()

#criar Tabelas

class Usuario(Base):
    __tablename__="usuarios"
    
    id = Column("id",Integer,primary_key=True, autoincrement=True)
    nome =Column("nome",String)
    senha= Column("senha",String)
    email =Column("email",String)
    senha= Column("senha",String)
    ativo= Column("ativo",Boolean)

    def __init__(self,nome,senha,email,ativo=True):
        self.nome = nome
        self.senha =senha
        self.email =email
        self.ativo = ativo
        
#livros

class Livro(Base):
    __tablename__="livros"
     
    id = Column("id",Integer,primary_key=True, autoincrement=True)
    titulo=Column("titulo",String)
    qtde_pag=Column("qtde_pag",Integer)
    dono=Column("dono",ForeignKey("usuarios.id"))

    def __init__(self,titulo,qtde_pag,dono):
        self.titulo = titulo
        self.qtde_pag =qtde_pag
        self.dono =dono
        


Base.metadata.create_all(bind=db)


#CRUD

# usuario = Usuario("Matheus","matheus@123","123")

# session.add(usuario)
# session.commit()

#Read
# lista_usuarios=session.query(Usuario).first()

# lista_usuarios =lista_usuarios.id


# livro = Livro("Harry Potter","863",lista_usuarios)

# session.add(livro)
# session.commit()

#update
mail=session.query(Usuario).all()

mail[0].email ="matheusssscf@gmail.com"


session.commit()