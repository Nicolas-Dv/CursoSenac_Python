continua = True
lista_respostas_aluno = []
qtdAlunosMenosDezVezes= 0
qtdAlunosDezQuinzeVezes = 0
qtdAlunosMaisQuinzeVezes = 0

while continua:
    numero_vezes = int(input("Quantas vezes voc~e utilizou o restaurante? Resposta: "))
    lista_respostas_aluno.append(numero_vezes)

    teste_nova_pergunta = input("\nDeseja perguntar para outro aluno [S]im ou [N]: ")
    if teste_nova_pergunta.upper().startswith('N'):
        continua = False

for resposta in lista_respostas_aluno:
    if resposta < 10:
        qtdAlunosMenosDezVezes = qtdAlunosMenosDezVezes + 1
    elif resposta <= 15:
        qtdAlunosDezQuinzeVezes = qtdAlunosDezQuinzeVezes + 1
    else: 
        qtdAlunosMaisQuinzeVezes = qtdAlunosMaisQuinzeVezes + 1

qtd                        