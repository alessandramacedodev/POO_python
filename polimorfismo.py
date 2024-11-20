#Polimorfismo permite tratar os diferentes profissionais de saúde citados de forma 
# uniforme ao realizar atividades comuns, como atendimento.


def teste_atendimento(profissional):
    profissional.atender_paciente()
    profissional.registrar_prescricao("Paciente João", "Paracetamol 500mg")

# Testes
class Medico:
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade

    def atender(self):
        return f"{self.nome} está atendendo na especialidade {self.especialidade}."

class Enfermeiro:
    def __init__(self, nome, coren, setor):
        self.nome = nome
        self.coren = coren
        self.setor = setor

    def atender(self):
        return f"{self.nome} está atendendo no setor {self.setor}."

def teste_atendimento(profissional):
    print(profissional.atender())

# Código Principal
medico = Medico("Dr. Carlos", "CRM12345", "Cardiologia")
enfermeiro = Enfermeiro("Enf. Julia", "COREN54321", "Emergência")

print("Testando o Médico:")
teste_atendimento(medico)

print("\nTestando o Enfermeiro:")
teste_atendimento(enfermeiro)
