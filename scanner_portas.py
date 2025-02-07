import socket

# Função para escanear um intervalo de portas
def scanner_portas(ip, portas):
    for porta in portas:
        # Tenta conectar à porta
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((ip, porta))
        if resultado == 0:
            print(f"Porta {porta} está ABERTA")
        else:
            print(f"Porta {porta} está FECHADA")
        s.close()

# Função principal
def main():
    ip = input("Digite o IP ou domínio para escanear: ")
    
    # Escaneando um intervalo de portas comuns
    portas_comuns = [21, 22, 23, 25, 53, 80, 443, 8080]
    print(f"Iniciando escaneamento nas portas {portas_comuns} do host {ip}...\n")
    
    # Chama a função para escanear
    scanner_portas(ip, portas_comuns)

# Executando o script
if __name__ == "__main__":
    main()