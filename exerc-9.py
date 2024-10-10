# Função para calcular o custo final ao consumidor
def calcular_custo_final():
    # Passo 2: Ler o custo de fábrica
    custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
    
    # Passo 3: Calcular a porcentagem do distribuidor (28%)
    custo_distribuidor = custo_fabrica * 0.28
    
    # Passo 4: Calcular os impostos (45%)
    custo_impostos = custo_fabrica * 0.45
    
    # Passo 5: Calcular o custo final ao consumidor
    custo_final = custo_fabrica + custo_distribuidor + custo_impostos
    
    # Passo 6: Exibir o custo final
    print(f"O custo final ao consumidor é: R$ {custo_final:.2f}")

# Chamada da função
calcular_custo_final()
