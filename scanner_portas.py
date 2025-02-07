import socket
import threading

# Função para escanear uma porta específica
def escanear_porta(ip, porta, arquivo_log):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        resultado = s.connect_ex((ip, porta))
        
        if resultado == 0:
            status = f"Porta {porta} está ABERTA"
        else:
            status = f"Porta {porta} está FECHADA"
        
        print(status)
        arquivo_log.write(status + "\n")
        s.close()
    except Exception as e:
        print(f"Erro ao escanear a porta {porta}: {e}")

# Função para iniciar o escaneamento
def iniciar_scanner():
    ip = input("Digite o IP ou domínio para escanear: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))
    
    print(f"\nEscaneando {ip} nas portas {porta_inicial} a {porta_final}...\n")
    
    with open("resultado.txt", "w") as arquivo_log:
        threads = []

        for porta in range(porta_inicial, porta_final + 1):
            thread = threading.Thread(target=escanear_porta, args=(ip, porta, arquivo_log))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    print("\nEscaneamento concluído! Os resultados foram salvos em 'resultado.txt'.")

# Função para exibir os resultados salvos
def ler_resultados():
    try:
        with open("resultado.txt", "r") as arquivo:
            print("\nResultados do último escaneamento:\n")
            print(arquivo.read())
    except FileNotFoundError:
        print("\nNenhum escaneamento foi realizado ainda.")

# Menu interativo
def menu():
    while True:
        print("\n===== Scanner de Portas =====")
        print("1 - Iniciar escaneamento")
        print("2 - Ler resultados salvos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_scanner()
        elif opcao == "2":
            ler_resultados()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executando o menu
if __name__ == "__main__":
    menu()