numbers = []

for c in range(0, 5):
    num = int(input('Digite um número: ')) # recebe os valores

    if c == 0 or num > numbers[-1]: 
    #se a lista estiver vazia ou o valor for maior ao último valor, adicione no final
        numbers.append(num)
        print('adicionado ao final da lista...')
    else:
        position = 0
        while position < len(numbers):
            if num <= numbers[position]:
                numbers.insert(position, num)
                print(f'adicinado na posição {position} da lista...')
                break
            position += 1

print(f'Os valores digitados em ordem crescente foram: {numbers}.')
