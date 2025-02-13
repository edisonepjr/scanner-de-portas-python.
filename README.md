<h1 align="center">🔍 Scanner de Portas Python</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Python&message=3.x&color=blue&style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/static/v1?label=Status&message=Em%20Desenvolvimento&color=red&style=for-the-badge"/>
  <img src="https://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/edisonepjr/scanner-de-portas-python?style=social"/>
</p>

> Status do Projeto: 🚧 **Em Desenvolvimento**

---

## 📌 **Índice**  

- [Sobre o Projeto](#sobre-o-projeto)  
- [Casos de Uso](#casos-de-uso)  
- [Funcionalidades](#funcionalidades)  
- [Demonstração](#demonstração)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação e Uso](#instalação-e-uso)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  

---

## 📖 **Sobre o Projeto**  

O **Scanner de Portas Python** é uma ferramenta desenvolvida para auxiliar profissionais de segurança cibernética, administradores de redes e entusiastas da tecnologia na verificação de portas abertas em um determinado host.  

Através do uso da biblioteca **socket**, este scanner realiza verificações eficientes para identificar serviços ativos, ajudando na detecção de vulnerabilidades e no monitoramento de redes.

🔹 **Tecnologia principal:** Python  
🔹 **Foco:** Segurança cibernética e monitoramento de rede  
🔹 **Tipo:** Ferramenta CLI (Command Line Interface)  

---

## 🎯 **Casos de Uso**  

🔹 **Caso 1: Análise de Segurança em um Servidor Local**  
📌 **Usuário:** Administrador de Rede  
📌 **Objetivo:** Identificar portas abertas em um servidor dentro da rede local  

**Exemplo de uso:**  
```bash
python scanner_portas.py 192.168.1.1

Saída esperada:

[+] 80 (HTTP) - Aberta
[+] 443 (HTTPS) - Aberta
[-] 22 (SSH) - Fechada

---

🔹 Caso 2: Auditoria de um site público

📌 Usuário: Especialista em segurança cibernética
📌 Objetivo: Identificar quais serviços estão rodando em um site público
📌 Exemplo de uso:

python scanner_portas.py example.com

Saída esperada:

[+] 80 (HTTP) - Aberta
[+] 443 (HTTPS) - Aberta
[-] 3306 (MySQL) - Fechada


## 🔧 Funcionalidades

- Verificação de portas abertas
- Identificação de serviços ativos
- Relatórios detalhados de auditoria

---

## 💻 Demonstração

![Demonstração](https://link-para-a-imagem-da-demonstracao.com)

---

## 📋 Pré-requisitos

- Python 3.x

---

## 🚀 Instalação e Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/edisonepjr/scanner-de-portas-python.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd scanner-de-portas-python
   ```

3. Execute o script:
   ```bash
   python scanner_portas.py <endereço IP ou domínio>
   ```

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades! Basta seguir os passos abaixo:

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

