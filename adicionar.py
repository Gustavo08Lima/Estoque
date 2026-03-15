import json




"""     Função de adicionar os dados """
def adicionar_nova_cor(categoria, nova_cor,tamanho, dados):
    # 1. Carrega o dicionário completo
    with open('produtos.json', 'r', encoding="utf-8") as f:
        estoque = json.load(f)

   
    if categoria not in estoque:
        estoque[categoria] = {}
    
    if nova_cor not in estoque[categoria]:
        estoque[categoria][nova_cor] = {}
    
    if tamanho not in estoque[categoria]:
        estoque[categoria][nova_cor][tamanho] = {}
    
   

    # Note que não usamos append, usamos o sinal de =
    estoque[categoria][nova_cor][tamanho] = dados
   
    

    # 3. Salva de volta
    with open('produtos.json', 'w', encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

   













