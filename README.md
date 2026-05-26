🐍 Python User System

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Sistema simples e funcional de cadastro de usuários executado no terminal.  
Desenvolvido em Python para fins de estudo, portfólio e prática de lógica de programação.
---

 Funcionalidades

- Cadastrar usuário – nome e e-mail com validação de campos vazios e e-mail duplicado  
- Listar usuários – exibe todos os usuários cadastrados com ID, nome e e-mail  
- Buscar usuário – por parte do nome (case‑insensitive) ou e-mail exato  
- Menu interativo – loop com opções numéricas e tratamento de erro  
- Armazenamento em memória – utilizando lista de dicionários  

---
🚀 Como executar:

1. Acesse o repositório:  
   https://github.com/jessica-oliver28/python-user-system

2. Clique em **Code** → **Download ZIP**

3. Extraia a pasta e abra o terminal dentro dela.

4. Execute o comando:  
   python main.py

   
🧠 Exemplo de uso
===== SISTEMA DE CADASTRO DE USUÁRIOS =====
1 - Cadastrar usuário
2 - Listar usuários
3 - Buscar usuário
0 - Sair
Escolha uma opção: 1

--- Cadastro de Novo Usuário ---
Nome: Ana Silva
E-mail: ana@email.com
Usuário Ana Silva cadastrado com sucesso! ID: 1

--- (menu novamente) ---
Escolha uma opção: 2

--- Lista de Usuários ---
ID: 1 | Nome: Ana Silva | E-mail: ana@email.com

--- (busca) ---
Escolha uma opção: 3
Digite o nome (ou parte) ou e-mail: ana
Encontrado(s) 1 usuário(s):
ID: 1 | Nome: Ana Silva | E-mail: ana@email.com

Organização interna do main.py

cadastrar_usuario(): solicita nome/email, valida e adiciona à lista
listar_usuarios(): percorre a lista e exibe os dados formatados
buscar_usuario(): busca por substring (nome) ou e-mail exato
menu(): loop principal com opções e controle do programa
if __name__ ..: garante execução apenas quando o arquivo é rodado

👤 Autora:
Jéssica Oliveira

GitHub: github.com/jessica-oliver28

LinkedIn: linkedin.com/in/jessica-oliveira-frontend

Projeto desenvolvido como parte do portfólio pessoal de Python.





