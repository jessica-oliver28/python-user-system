usuarios = []

def cadastrar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio. Cadastro cancelado.")
        return

    email = input("Email: ").strip()
    if not email:
        print("Email não pode ser vazio. Cadastro cancelado.")
        return


    for usuario in usuarios:
        if usuario["email"] == email:
            print("Email já cadastrado. Cadastro cancelado.")
            return

    novo_id = len(usuarios) + 1
    usuario = {"id": novo_id, "nome": nome, "email": email}
    usuarios.append(usuario)
    print(f"Usuário {nome} Cadastrado com sucesso! ID: {novo_id}")

def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado")
        return
    for usuario in usuarios:
        print(f"ID: {usuario["id"]} | Nome: {usuario["nome"]} | Email: {usuario["email"]}")

def buscar_uuario():
    print("\n--- Buscar Usuário ---")
    termo = input("Digite nome (parte) ou email: ").strip().lower()
    if not termo:
        print("Termo vazio.")
        return
    resultados= []
    for usuario in usuarios:
        if termo in usuario["nome"].lower() or termo == usuario["email"].lower(): resultados.append(usuario)
    if resultados:
        print(f"Encontrados {len(resultados)}:")
        for u in resultados:
            print(f"ID: {u["id"]} | {u["nome"]} | {u["email"]}")
    else:
        print("Nenhum encontrado.")

def menu():
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1 - Cadastrar\n2 - Listar\n3 - Buscar\n0 - Sair")
        opcao= input("Opção: ").strip()
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_uuario()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Inválido. Use 1, 2, 3 0.")

if __name__ == "__main__":
    menu()