import json


#BIBLIOTECA

"""     Função de adicionar os dados """
def adicionar_nova_cor(categoria, nova_cor,tamanho, dados):
    # Abre o json com o comando 'r'
    with open('produtos.json', 'r', encoding="utf-8") as f: 
        estoque = json.load(f) 

    
   # Faz uma condição para que se nao tiver nenhum item com o nome criado, criasse um novo item
    if categoria not in estoque:
        estoque[categoria] = {}
   
    if nova_cor not in estoque[categoria]:
        estoque[categoria][nova_cor] = {}
    
    if tamanho not in estoque[categoria]:
        estoque[categoria][nova_cor][tamanho] = {}
    
   

    # aqui adicionamos dados dentro do dicionario, usando = em vez de append
    estoque[categoria][nova_cor][tamanho] = dados
   
    

    # 3. Salva o json com o comando 'w' e volta
    with open('produtos.json', 'w', encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

   













