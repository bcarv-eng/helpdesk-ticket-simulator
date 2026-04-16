# main.py
# Simulador de abertura de chamados de suporte técnico
# Desenvolvido por Barbara Carvalho

import datetime

def registrar_chamado():
    """
    Coleta os dados do usuário, gera timestamp e armazena as informações
    em um arquivo de log (chamados.txt).
    """
    print("=" * 50)
    print("ABERTURA DE CHAMADO - SERVICE DESK".center(50))
    print("=" * 50)

    usuario = input("Nome do usuário: ").strip()
    setor = input("Setor: ").strip()
    problema = input("Descrição do problema: ").strip()

    if not usuario or not problema:
        print("\nErro: os campos 'Nome do usuário' e 'Descrição do problema' são obrigatórios.")
        return

    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    registro = f"{data_hora} | Usuário: {usuario} | Setor: {setor} | Problema: {problema}\n"

    with open("chamados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(registro)

    print("\nChamado registrado com sucesso.")

    # Exibe a quantidade atual de chamados no arquivo
    try:
        with open("chamados.txt", "r", encoding="utf-8") as arquivo:
            total = len(arquivo.readlines())
        print(f"Total de chamados registrados até o momento: {total}")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    registrar_chamado()
    input("\nPressione Enter para encerrar...")
