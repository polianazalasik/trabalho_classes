import os
from peewee import *

arq = "agencia.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Agencia(BaseModel):
    nome_agencia = CharField()
    cnpj_agencia = IntegerField()

class Filial(BaseModel):
    agencia = ForeignKeyField(Agencia)
    localizacao_filial = CharField()

class Funcionario(BaseModel):
    id_func = IntegerField()
    nome_func = CharField()
    cargo_func = CharField()

class Cliente(BaseModel):
    nome_cliente = CharField()
    cpf_cliente = IntegerField()
    nacionalidade_cliente = CharField()

class Seguro(BaseModel):
    tipo_seguro = CharField()
    cliente = ForeignKeyField(Cliente)

class Pedido(BaseModel):
    meio_de_pedido = CharField()

class Destino(BaseModel):
    nome_destino = CharField()
    localizacao_destino = CharField()

class Pacote(BaseModel):
    destino = ForeignKeyField(Destino)
    data_viagem = CharField()
    data_volta = CharField()
    preco_pacote = FloatField()

class Hotel(BaseModel):
    nome_hotel = CharField()
    localizacao_hotel = CharField()
    qtd_dias = IntegerField()

class TipoViagem(BaseModel):
    tipo_de_viagem = CharField()
    veiculo = CharField()

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Agencia,
                Filial,
                Funcionario,
                Cliente,
                Seguro,
                Pedido,
                Destino,
                Pacote,
                Hotel,
                TipoViagem
])

cvc = Agencia.create(nome_agencia = "CVC", cnpj_agencia = 456789)

filial_salvador = Filial.create(agencia = cvc, localizacao_filial = "Rua Arthur de Azevêdo Machado, 3443 - 1004 - Costa Azul, Salvador - BA, 41760-000")

jose_func = Funcionario.create(id_func = 32, nome_func = "José De Amaral Silveira", cargo = "Vendedor")

maria_cliente = Cliente.create(nome_cliente = "Maria Eduarda Da Costa", cpf_cliente = 99876432191, nacionalidade = "Portuguesa")

vida_seguro = Seguro.create(tipo_seguro = "Vida", cliente = maria_cliente)

loja_pedido = Pedido.create(meio_de_pedido = "Físico")

saopaulo = Destino.create(nome_destino = "MASP", localizacao_destino = "Avenida Paulista, 1578 | Jardins, São Paulo, Estado de São Paulo 01310-200, Brasil")

pacote1 = Pacote.create(destino = saopaulo, data_viagem = "06/12/2019", data_volta = "08/12/2019", preco_pacote = 800.00)

hotel_paulista = Hotel.create(nome_hotel = "Hotel Paulista Wall Street", localizacao_hotel = "R. Itapeva, 636 - Bela Vista, São Paulo - SP, 01332-000", qtd_dias = 2)

terrestre = TipoViagem.create(tipo_de_veiculo = "Terrestre", veiculo = "Ônibus")

