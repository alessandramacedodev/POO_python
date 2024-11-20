# Composição permite construir classes complexas. 
# por exemplo, um Hospital pode ser composto por várias U
# unidades que possuem diferentes equipamentos e profissionais.


class Unidade:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Hospital:
    def __init__(self, nome):
        self.nome = nome
        self.unidades = []

    def adicionar_unidade(self, unidade):
        self.unidades.append(unidade)

    def listar_unidades(self):
        print(f"Unidades do hospital {self.nome}:")
        for unidade in self.unidades:
            print(f"- {unidade.nome} ({unidade.tipo})")

# Testes
hospital = Hospital("Hospital Central")
uti = Unidade("Unidade de Terapia Intensiva", "UTI")
emergencia = Unidade("Emergência", "Atendimento de Urgência")

hospital.adicionar_unidade(uti)
hospital.adicionar_unidade(emergencia)
hospital.listar_unidades()
