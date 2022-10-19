def cpf_validate(cpf):
    # verifica se são apenas números digitados e transforma os caracteres em int para que a função funcione
    cpf = [int(char) for char in cpf if char.isdigit()]

    # verifica se tem 11 digitos
    if len(cpf) != 11:
        return False

    # casos que digitam o mesmo numero repetidamente EX: 11111111111
    if cpf == cpf[::-1]:
        return False
    
    #  Area pra validar os 2 digitos:
    for i in range(9, 11):
        valor = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
        else:
            return True

cpf = input("Informe o CPF a ser consultado: ")

if cpf_validate(cpf):
    print("O CPF é válido!")
else:
    print("O CPF é inválido, tente novamente!")