praias = {}
dados_praia = []
continua = 0 

while continua == 0:
    nome_praia = input("Informe o nome da praia: ")
    distancia_centro = float(input("Informe a distância da praia ao centro da cidade: "))
    media_veranistas = float(input("Informe o número médio de veranistas na praia: "))
    tipo_acesso = float(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado; 1 - acesso asfaltado): "))

    praias[nome_praia] = [distancia_centro, media_veranistas, tipo_acesso]

    continua = int(input("\nDeseja cadastrar nova praia (0 - Sim / 1 - Não): "))
    print()

print(praias)
