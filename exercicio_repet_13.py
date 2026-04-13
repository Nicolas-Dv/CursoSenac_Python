class Candidato:
    
    def __init__(self, nome, nota_portugues, nota_matematica, nota_conhecimentos_gerais):
        self.nome = nome
        self.nota_portugues = nota_portugues
        self.nota_matematica = nota_matematica
        self.nota_conhecimentos_gerais = nota_conhecimentos_gerais
        self.media = 0.0
        self.situacao = "Reprovado"
    
    def __str__(self):
        return f"{nome}"
    
candidatos = []    

continua = 0
while continua == 0:
    nome = input("Informe o nome do Candidato: ")
    nota_portugues = float(input("Informe a nota de Português: "))
    nota_matematica = float(input("Informe a nota de Matemática: "))
    nota_conhecimentos_gerais = float(input("Informe a nota de Conhecimentos Gerais): "))

    candidato = Candidato(nome, nota_portugues, nota_matematica, nota_conhecimentos_gerais)

    candidatos.append(candidato)


    continua = int(input("\nDeseja cadastrar novo Candidato (0 - Sim / Qualquer outro número - Não"))
    print()

# for candidato in candidatos:
#     print(candidatos) 

lista_nomes_aprovados = []

for candidato in candidatos:
    media = (candidato.nota_portugues + candidato.nota_matematica + candidato.nota_conhecimentos_gerais) / 3
    candidato.media = media

    if candidato.nota_portugues < 2.0 or candidato.nota_matematica < 2.0 or candidato.nota_conhecimentos_gerais < 2.0:
        candidato_tem_nota_abaixo_2 = True
    else:
        candidato_tem_nota_abaixo_2 = False    

    if media > 4.0 and candidato_tem_nota_abaixo_2 == False:
        candidato.situacao = "Aprovado"
        lista_nomes_aprovados.append(candidato.nome)
        

for candidato in candidatos:
    print( f"Candidato: {candidato.nome} obteve média igual a {candidato.media} e está {candidato.situacao}")             
 
print("Candidatos aprovados:", lista_nomes_aprovados)

