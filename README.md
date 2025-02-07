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