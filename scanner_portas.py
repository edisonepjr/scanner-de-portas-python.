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

# Função principal
def main():
    ip = input("Digite o IP ou domínio para escanear: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))
    
    print(f"\nEscaneando {ip} nas portas {porta_inicial} a {porta_final}...\n")
    
    with open("resultado.txt", "w") as arquivo_log:
        threads = []

        # Criando uma thread para cada porta
        for porta in range(porta_inicial, porta_final + 1):
            thread = threading.Thread(target=escanear_porta, args=(ip, porta, arquivo_log))
            threads.append(thread)
            thread.start()

        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()

    print("\nEscaneamento concluído! Os resultados foram salvos em 'resultado.txt'.")

# Executando o script
if __name__ == "__main__":
    main()