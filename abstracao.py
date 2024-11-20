# A abstração foca nos aspectos essenciais de um objeto, 
# ocultando detalhes de implementação. A classe abstrata 
# define a estrutura que suas subclasses devem seguir.


from abc import ABC, abstractmethod

class ProfissionalSaude(ABC):
    def __init__(self, nome, registro, especialidade):
        self.nome = nome
        self.registro = registro
        self.especialidade = especialidade

    @abstractmethod
    def atender_paciente(self):
        pass

    @abstractmethod
    def registrar_prescricao(self, paciente, prescricao):
        pass
