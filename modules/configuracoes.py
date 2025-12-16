import json
caminho_json = r"config\settings.json"

class Configuracao:
    def mudar_configuracao(atributo):
        if atributo == 1:
            preco = float(input("Qual o novo preço da gasolina? "))
            with open(caminho_json, "r") as f:
                dados = json.load(f)
                dados["configs"]["abastecimentos"]["valor_gasolina"] = preco

            with open(caminho_json, "w") as f:
                json.dump(dados, f, indent=4)

        elif atributo == 2:
            escolha = str(input("1 - Peso por tipo de veículo\n2 - Custo por tipo de manutenção\n"))
            if escolha == 1:
                veiculo = str(input("Diga o tipo de veículo: "))
                veiculo = veiculo.lower()
                if veiculo == "carro" or veiculo == "moto" or veiculo == "caminhao":
                    peso = int(input(f"Qual o novo peso do {veiculo}? "))
                    with open(caminho_json, "r") as f:
                        dados = json.load(f)
                    dados["configs"]["manutencoes"]["peso"][veiculo] = peso
                    with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
                        print("Peso, alterado.")
                else:
                    print("Tipo de veículo inválido.")
            elif escolha == 2:
                print("1 - Preventiva\n2 - Corretiva")
                tipo = int(input("Diga o tipo de manutenção: "))
                if tipo == 1:
                    preco = float(input("Qual o valor? "))
                    with open(caminho_json, "w") as f:
                        dados = json.load(f)
                    dados["configs"]["manutencoes"]["custo"]["preventiva"] = preco
                    with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
                elif tipo == 2:
                    preco = float(input("Qual o valor? "))
                    with open(caminho_json, "w") as f:
                        dados = json.load(f)
                    dados["configs"]["manutencoes"]["custo"]["corretiva"] = preco
                    with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
                else:
                    print("Escolha inválida.")

        elif atributo == 3:
            print("1 - Moto\n2 - Carro\n3 - Caminhão")
            escolha = int(input("Qual a sua escolha? "))
            if escolha == 1:
                cnh = str(input("Qual a nova categoria de CNH da moto? "))
                cnh = cnh.upper()
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["compatibilidade"]["moto"] = cnh
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
            elif escolha == 2:
                cnh = str(input("Qual a nova categoria de CNH do carro? "))
                cnh = cnh.upper()
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["compatibilidade"]["carro"] = cnh
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
            elif escolha == 3:
                cnh = str(input("Qual a nova categoria de CNH do caminhão? "))
                cnh = cnh.upper()
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["compatibilidade"]["caminhao"] = cnh
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
            else:
                print("Escolha inválida.")

        elif atributo == 4:
            limite = float(input("Digite o novo limite de quilometragem para manuteção: "))
            with open(caminho_json, "r") as f:
                dados = json.load(f)
            dados["configs"]["quilometragem"]["limite"] = limite
            with open(caminho_json, "w") as f:
                    json.dump(dados, f, indent=4)

        elif atributo == 5:
            print("1 - Carro\n2 - Moto\n3 - Caminhão")
            escolha = int(input("Qual sua escolha?"))
            if escolha == 1:
                minimo = float(input("Qual o consumo minimo? "))
                maximo = float(input("Qual o consumo maximo? "))
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["abastecimentos"]["consumo_medio"]["carro"]["minimo"] = minimo
                dados["configs"]["abastecimentos"]["consumo_medio"]["carro"]["maximo"] = maximo
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
            if escolha == 2:
                minimo = float(input("Qual o consumo minimo? "))
                maximo = float(input("Qual o consumo maximo? "))
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["abastecimentos"]["consumo_medio"]["moto"]["minimo"] = minimo
                dados["configs"]["abastecimentos"]["consumo_medio"]["moto"]["maximo"] = maximo
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
            if escolha == 3:
                minimo = float(input("Qual o consumo minimo? "))
                maximo = float(input("Qual o consumo maximo? "))
                with open(caminho_json, "r") as f:
                    dados = json.load(f)
                dados["configs"]["abastecimentos"]["consumo_medio"]["caminhao"]["minimo"] = minimo
                dados["configs"]["abastecimentos"]["consumo_medio"]["caminhao"]["maximo"] = maximo
                with open(caminho_json, "w") as f:
                        json.dump(dados, f, indent=4)
