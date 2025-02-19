import math

def calcular_tamanho_vetor(vetor):
    return math.sqrt(vetor[0]**2 + vetor[1]**2 + vetor[2]**2)

def normalizar_vetor(vetor):
    tamanho = calcular_tamanho_vetor(vetor)
    if tamanho == 0:
        return [0, 0, 0]
    return [vetor[0] / tamanho, vetor[1] / tamanho, vetor[2] / tamanho]

def adicionar_vetores(vetor1, vetor2):
    return [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1], vetor1[2] + vetor2[2]]

def subtrair_vetores(vetor1, vetor2):
    return [vetor1[0] - vetor2[0], vetor1[1] - vetor2[1], vetor1[2] - vetor2[2]]

def multiplicar_escalar_vetor(escalar, vetor):
    return [escalar * vetor[0], escalar * vetor[1], escalar * vetor[2]]

def dividir_vetor_por_escalar(escalar, vetor):
    if escalar == 0:
        return [0, 0, 0]
    return [vetor[0] / escalar, vetor[1] / escalar, vetor[2] / escalar]

def calcular_produto_escalar(vetor1, vetor2):
    return vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1] + vetor1[2] * vetor2[2]

def formatar_vetor(vetor):
    return [f"{x:.2f}" for x in vetor]

def main():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    vetor = [x, y, z]

    while True:
        print("\nMenu de opções:")
        print("1) Calcular o tamanho do vetor")
        print("2) Normalizar o vetor")
        print("3) Adicionar outro vetor")
        print("4) Subtrair outro vetor")
        print("5) Multiplicar vetor por escalar")
        print("6) Dividir vetor por escalar")
        print("7) Calcular o produto escalar")
        print("8) Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == '1':
            tamanho = calcular_tamanho_vetor(vetor)
            print(f"O tamanho do vetor é: {tamanho:.2f}")

        elif opcao == '2':
            vetor_normalizado = normalizar_vetor(vetor)
            print(f"Vetor normalizado: {formatar_vetor(vetor_normalizado)}")

        elif opcao == '3':
            x2 = float(input("Digite o valor de x do novo vetor: "))
            y2 = float(input("Digite o valor de y do novo vetor: "))
            z2 = float(input("Digite o valor de z do novo vetor: "))
            novo_vetor = [x2, y2, z2]
            vetor = adicionar_vetores(vetor, novo_vetor)
            print(f"Vetor resultante: {formatar_vetor(vetor)}")

        elif opcao == '4':
            x2 = float(input("Digite o valor de x do novo vetor: "))
            y2 = float(input("Digite o valor de y do novo vetor: "))
            z2 = float(input("Digite o valor de z do novo vetor: "))
            novo_vetor = [x2, y2, z2]
            vetor = subtrair_vetores(vetor, novo_vetor)
            print(f"Vetor resultante: {formatar_vetor(vetor)}")

        elif opcao == '5':
            escalar = float(input("Digite o valor do escalar: "))
            vetor = multiplicar_escalar_vetor(escalar, vetor)
            print(f"Vetor resultante: {formatar_vetor(vetor)}")

        elif opcao == '6':
            escalar = float(input("Digite o valor do escalar: "))
            vetor = dividir_vetor_por_escalar(escalar, vetor)
            print(f"Vetor resultante: {formatar_vetor(vetor)}")

        elif opcao == '7':
            x2 = float(input("Digite o valor de x do novo vetor: "))
            y2 = float(input("Digite o valor de y do novo vetor: "))
            z2 = float(input("Digite o valor de z do novo vetor: "))
            novo_vetor = [x2, y2, z2]
            produto_escalar = calcular_produto_escalar(vetor, novo_vetor)
            print(f"Produto escalar: {produto_escalar:.2f}")

        elif opcao == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()