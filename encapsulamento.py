#Encapsulamento tem o objetivo de proteger os dados internos 
# de uma classe. Em um sistema de saúde, isso garante que informações 
# sensíveis, como prontuários médicos, sejam acessadas apenas por 
# métodos controlados.


class Paciente:
    def __init__(self, id_paciente, nome, idade, prontuario):
        self._id_paciente = id_paciente  # Atributo privado
        self._nome = nome                # Atributo privado
        self._idade = idade              # Atributo privado
        self._prontuario = prontuario    # Atributo privado

    def atualizar_idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Idade inválida.")

    def acessar_prontuario(self):
        return f"Prontuário de {self._nome}: {self._prontuario}"

# Testes
paciente = Paciente(1, "Ana Silva", 34, "Histórico: Diabetes tipo 2.")
paciente.atualizar_idade(35)
print(paciente.acessar_prontuario())
paciente.atualizar_idade(-5)  # Teste de validação
