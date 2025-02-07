import socket  # Importa a biblioteca de sockets do Python para realizar a conexão

def scan_port(host, port):
    """
    Função que verifica se uma porta está aberta no host especificado.
    :param host: Endereço IP ou domínio do host.
    :param port: Número da porta a ser verificada.
    :return: True se a porta estiver aberta, False se estiver fechada.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket para IPv4 e TCP
    s.settimeout(1)  # Define um tempo limite de 1 segundo para a tentativa de conexão
    result = s.connect_ex((host, port))  # Tenta conectar à porta do host
    s.close()  # Fecha o socket após a tentativa
    return result == 0  # Se o código de retorno for 0, a porta está aberta

def main():
    """
    Função principal que pede o endereço IP e escaneia as portas do host.
    """
    host = input("Digite o endereço IP ou domínio do host: ")  # Solicita o IP ou domínio do usuário
    portas = [21, 22, 23, 25, 53, 80, 110, 443, 8080]  # Lista de portas comuns a serem escaneadas
    print(f"Escaneando host {host}...\n")
    
    # Para cada porta na lista, verifica se está aberta ou fechada
    for port in portas:
        if scan_port(host, port):
            print(f"Porta {port} está ABERTA.")
        else:
            print(f"Porta {port} está FECHADA.")

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o script
