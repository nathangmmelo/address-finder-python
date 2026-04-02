import requests

# — Função 1: busca por CEP —————————————————————————
def buscar_cep(cep):
    cep = cep.replace("-", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido! Use 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"\n  CEP:        {dados['cep']}")
            print(f"  Logradouro: {dados['logradouro']}")
            print(f"  Bairro:     {dados['bairro']}")
            print(f"  Cidade:     {dados['localidade']} - {dados['uf']}")
            print(f"  DDD:        {dados['ddd']}\n")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")


# — Função 2: busca por endereço ————————————————————
def buscar_endereco(uf, cidade, logradouro):
    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if not dados:
            print("Nenhum endereço encontrado.")
            return

        print(f"\n  {len(dados)} resultado(s) encontrado(s):")

        for item in dados:
            print(f"\n  CEP:        {item['cep']}")
            print(f"  Logradouro: {item['logradouro']}")
            print(f"  Bairro:     {item['bairro']}")
            print(f"  Cidade:     {item['localidade']} - {item['uf']}")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")


# — Menu principal ——————————————————————————————————
while True:
    print("\n===== BUSCADOR DE CEP =====")
    print("1 - Buscar endereço pelo CEP")
    print("2 - Buscar CEP pelo endereço")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        cep = input("Digite o CEP: ")
        buscar_cep(cep)

    elif opcao == "2":
        uf = input("Estado (ex: SP): ").upper()
        cidade = input("Cidade (ex: SaoPaulo): ")
        logradouro = input("Logradouro (ex: AvenidaPaulista): ")
        buscar_endereco(uf, cidade, logradouro)

    elif opcao == "0":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")