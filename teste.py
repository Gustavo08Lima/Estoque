

valor = [ 20, 39, 50, 60]
quantidade = [30,20, 30]



for i  in valor:

    if i < 50:
        result = list(map(lambda x: round((x - (x*0.18) - ( x* 0.02) - 4 ),2), valor))
    else:
        result = list(map(lambda x: round((x - (x*0.14) - ( x* 0.02) - 20 ),2), valor))


qtd = list(map(lambda x: round((x*0.45),2), quantidade))

soma = list(map(lambda x,y: x - y, result, qtd))



print(f"Valor Desc {result}\n")
print(f"custo {qtd}\n")
print(f"total {soma}")