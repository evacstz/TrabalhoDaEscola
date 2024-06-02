nome = input("Escreva o nome do aluno: ")
disciplina = input("Escreva o nome da disciplina: ")
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
m = (nota1 + nota2) /2

print(f'A média do aluno é {m}')
if(m >= 6):
    situacao = "aprovado"
    print(f'{nome} está {situacao} na disciplina de {disciplina}')

else:
    situacao = "reprovado"
    print(f'{nome} está {situacao} na disciplina de {disciplina}')