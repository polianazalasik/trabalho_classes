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

    def __str__(self):
        return self.nome_agencia + " possui o CNPJ " + str(self.cnpj_agencia)

class Filial(BaseModel):
    agencia = ForeignKeyField(Agencia)
    localizacao_filial = CharField()

    def __str__(self):
        return "A agência " + str(self.agencia) + " com a filial em " + self.localizacao_filial

class Funcionario(BaseModel):
    id_func = IntegerField()
    nome_func = CharField()
    cargo_func = CharField()

    def __str__(self):
        return "O funcionário " + str(self.id_func) + " do nome " + self.nome_func + " que ocupa o cargo " + self.cargo_func

class Cliente(BaseModel):
    nome_cliente = CharField()
    cpf_cliente = IntegerField()
    nacionalidade_cliente = CharField()

    def __str__(self):
        return self.nome_cliente + " do cpf " + str(self.cpf_cliente) + " de nacionalidade " + self.nacionalidade_cliente

class Seguro(BaseModel):
    tipo_seguro = CharField()
    cliente = ForeignKeyField(Cliente)

    def __str__(self):
        return "O seguro de " + self.tipo_seguro + " atende ao cliente " + str(self.cliente) 

class Pedido(BaseModel):
    meio_de_pedido = CharField()

    def __str__(self):
        return "O pedido foi feito " + self.meio_de_pedido 

class Destino(BaseModel):
    nome_destino = CharField()
    localizacao_destino = CharField()

    def __str__(self):
        return "O destino é " + self.nome_destino + " que se localiza em " + self.localizacao_destino

class Pacote(BaseModel):
    destino = ForeignKeyField(Destino)
    data_viagem = CharField()
    data_volta = CharField()
    preco_pacote = FloatField()

    def __str__(self):
        return str(self.destino) + " começa " + self.data_viagem + " e termina " + self.data_volta + " e o preço do pacote é" + str(self.preco_pacote)

class Hotel(BaseModel):
    nome_hotel = CharField()
    localizacao_hotel = CharField()
    qtd_dias = IntegerField()

    def __str__(self):
        return "O hotel " + self.nome_hotel + " localizado em " + self.localizacao_hotel + " hospeda " + str(self.qtd_dias) + " dias"

class TipoViagem(BaseModel):
    tipo_de_viagem = CharField()
    veiculo = CharField()

    def __str__(self):
        return "A viagem será " + self.tipo_de_viagem + " feita de " + self.veiculo

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

jose_func = Funcionario.create(id_func = 32, nome_func = "José De Amaral Silveira", cargo_func = "Vendedor")

maria_cliente = Cliente.create(nome_cliente = "Maria Eduarda Da Costa", cpf_cliente = 99876432191, nacionalidade_cliente = "Portuguesa")

vida_seguro = Seguro.create(tipo_seguro = "Vida", cliente = maria_cliente)

loja_pedido = Pedido.create(meio_de_pedido = "Físico")

saopaulo = Destino.create(nome_destino = "MASP", localizacao_destino = "Avenida Paulista, 1578 | Jardins, São Paulo, Estado de São Paulo 01310-200, Brasil")

pacote1 = Pacote.create(destino = saopaulo, data_viagem = "06/12/2019", data_volta = "08/12/2019", preco_pacote = 800.00)

hotel_paulista = Hotel.create(nome_hotel = "Hotel Paulista Wall Street", localizacao_hotel = "R. Itapeva, 636 - Bela Vista, São Paulo - SP, 01332-000", qtd_dias = 2)

terrestre = TipoViagem.create(tipo_de_viagem = "Terrestre", veiculo = "Ônibus")

print(filial_salvador)
print(jose_func)
print(vida_seguro)
print(loja_pedido)
print(pacote1)
print(hotel_paulista)
print(terrestre)