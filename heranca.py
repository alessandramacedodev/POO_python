#Herança permite criar classes derivadas 
#para diferentes tipos de profissionais de saúde, 
#reutilizando atributos e métodos da classe base.

class ProfissionalSaude:
    def __init__(self, nome):
        self.nome = nome


class Medico(ProfissionalSaude):
    def atender_paciente(self):
        print(f"Médico {self.nome} está atendendo um paciente.")

    def registrar_prescricao(self, paciente, prescricao):
        print(f"Prescrição para {paciente}: {prescricao}")


class Enfermeiro(ProfissionalSaude):
    def atender_paciente(self):
        print(f"Enfermeiro {self.nome} está realizando um procedimento.")

    def registrar_prescricao(self, paciente, prescricao):
        print(f"Enfermeiros não têm permissão para prescrever.")


# Exemplo de uso
medico = Medico("Dr. João")
medico.atender_paciente()
medico.registrar_prescricao("Maria", "Paracetamol 500mg")

enfermeiro = Enfermeiro("Enf. Ana")
enfermeiro.atender_paciente()
enfermeiro.registrar_prescricao("Carlos", "Dipirona")

