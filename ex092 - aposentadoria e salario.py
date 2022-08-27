dict = {}
nome = input('Digite o nome: ')
ano = int(input('Digite o ano de nascimento: '))
idade = 2022 - ano
dict['Nome'] = nome
dict['Idade'] = idade
ctps = int(input('Carteira de trabalho. (0 = não tem: '))

if ctps == 0:
    dict['Ctps'] = ctps
    print(f'O nome é: {dict["Nome"]}\n'
          f'A idade é: {dict["Idade"]}\n'
          f'Não possui carteira de trabalho.')
else:
    Ano_Contrato = int(input('Digite o ano de contratação: '))
    Salario = float(input('Digite o salário: '))
    dict['Contratacao'] = Ano_Contrato
    dict['Salario'] = Salario
    dict['Aposentadoria'] = (Ano_Contrato + 35) - ano
    dict['Ctps'] = ctps
    print(f'O nome é: {dict["Nome"]}\n'
          f'A idade é: {dict["Idade"]}\n'
          f'No da carteira de trabalho: {dict["Ctps"]}\n'
          f'O ano de contratação é: {dict["Contratacao"]}\n'
          f'O salário é: {dict["Salario"]}\n'
          f'A pessoa vai se apostar com: {dict["Aposentadoria"]} anos.')








