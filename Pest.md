def maior_numero(lista):
    maior_num = lista[0]

    for num in lista:
        if num > maior_num:
            maior_num = num
    

    return maior_num

numeros = [' - 3' ,' - 2', '- 1', '0', '1', '2', '3']
maior = maior_numero(numeros)

print(f'O maior número é: {maior}')
