# 1. A lista deve ficar FORA da função para não ser resetada
soma = []

def salva():
    # 2. Captura e converte com segurança
    transform = "10"
    integer = int(transform) if transform else 0 

    # 3. Adiciona na lista global
    soma.append(integer)
    
    # 4. Debug para você ver os índices crescendo no terminal
    print(f"Lista atual: {soma} | Último índice: {len(soma)-1}")

    # Agora você pode usar soma[-1] para pegar o valor atual 
    # ou a lista 'soma' inteira para salvar no JSON da Quadrado²Perfeito
salva()
salva()