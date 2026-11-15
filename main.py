from modelos import Cliente, Quarto, QuartoLuxo, Reserva
import re
from datetime import datetime

# ==========================================
# FUNÇÕES AUXILIARES DE FORMATAÇÃO E VALIDAÇÃO
# ==========================================

def formatar_cpf(documento):
    """Remove tudo que não é número e aplica a máscara do CPF: 000.000.000-00"""
    digitos = re.sub(r'\D', '', documento)
    if len(digitos) == 11:
        return f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}"
    return documento


def formatar_telefone(telefone):
    """Aplica máscara de telefone automaticamente (celular ou fixo)"""
    digitos = re.sub(r'\D', '', telefone)
    if len(digitos) == 11:
        return f"({digitos[:2]}) {digitos[2]} {digitos[3:7]}-{digitos[7:]}"
    elif len(digitos) == 10:
        return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"
    return telefone


def obter_data_valida(mensagem):
    """
    Permite que o usuário digite apenas números (ex: 25122026)
    ou com barras, formatando e validando automaticamente contra datas passadas.
    """
    while True:
        entrada = input(mensagem).strip()

        # Converte formato numérico compacto (8 dígitos) para DD/MM/AAAA
        digitos = re.sub(r'\D', '', entrada)
        if len(digitos) == 8:
            entrada = f"{digitos[:2]}/{digitos[2:4]}/{digitos[4:]}"

        try:
            data_obj = datetime.strptime(entrada, "%d/%m/%Y")

            # Impede datas no passado
            if data_obj.date() < datetime.now().date():
                print(">> A data não pode ser no passado. Tente novamente.")
                continue

            return data_obj.strftime("%d/%m/%Y")
        except ValueError:
            print(">> Data inválida! Digite no formato DD/MM/AAAA ou apenas os 8 números (ex: 25122026).")


# ==========================================
# FUNÇÃO PRINCIPAL: MENU DO SISTEMA
# ==========================================
def menu():
    # Inicialização das listas em memória
    clientes = []
    quartos = [
        Quarto(101, "Solteiro", 150.0),
        Quarto(102, "Casal", 250.0),
        QuartoLuxo(201, 450.0)  # Instância de QuartoLuxo (Polimorfismo)
    ]
    reservas = []

    while True:
        # Exibição do Menu Principal
        print("\n========================================")
        print("      SISTEMA DE RESERVAS DE HOTEL      ")
        print("========================================")
        print("1. Cadastrar Cliente")
        print("2. Listar Quartos")
        print("3. Realizar Reserva")
        print("4. Listar Reservas")
        print("5. Realizar Checkout (Liberar Quarto)")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            # ------------------------------------------
            # OPÇÃO 1: CADASTRO DE CLIENTE
            # ------------------------------------------
            if opcao == "1":
                print("\n--- Cadastro de Cliente ---")
                nome = input("Nome do cliente: ")

                doc_raw = input("Documento (CPF): ")
                documento = formatar_cpf(doc_raw)

                tel_raw = input("Contato (Telefone): ")
                contato = formatar_telefone(tel_raw)

                cliente = Cliente(nome, documento, contato)
                clientes.append(cliente)
                print(f">> Cliente cadastrado com sucesso! (CPF formatado: {documento})")

            # ------------------------------------------
            # OPÇÃO 2: LISTAGEM DE QUARTOS
            # ------------------------------------------
            elif opcao == "2":
                print("\n--- Lista de Quartos ---")
                for q in quartos:
                    status = "Disponível" if q.disponivel else "Ocupado"
                    print(f"Quarto {q.numero} | Tipo: {q.tipo} | Diária: R$ {q.preco_diaria:.2f} | Status: {status}")

            # ------------------------------------------
            # OPÇÃO 3: CRIAÇÃO DE RESERVA
            # ------------------------------------------
            elif opcao == "3":
                print("\n--- Nova Reserva ---")
                if not clientes:
                    print(">> Erro: Cadastre pelo menos um cliente antes de realizar reservas.")
                    continue

                doc_cliente = input("Digite o documento do cliente: ")
                doc_cliente_formatado = formatar_cpf(doc_cliente)
                
                # Busca o cliente considerando formato com ou sem máscara
                cliente_encontrado = next(
                    (c for c in clientes if c.documento == doc_cliente_formatado or c.documento == doc_cliente), None)

                if not cliente_encontrado:
                    print(">> Erro: Cliente não encontrado.")
                    continue

                num_quarto = int(input("Número do quarto desejado: "))
                quarto_encontrado = next((q for q in quartos if q.numero == num_quarto and q.disponivel), None)

                if not quarto_encontrado:
                    print(">> Erro: Quarto não encontrado ou já ocupado.")
                    continue

                # Coleta e validação de datas
                data_entrada = obter_data_valida("Data de entrada (DD/MM/AAAA ou DDMMAAAA): ")
                data_saida = obter_data_valida("Data de saída (DD/MM/AAAA ou DDMMAAAA): ")

                # Criação da reserva e alteração de estado do quarto
                reserva = Reserva(cliente_encontrado, quarto_encontrado, data_entrada, data_saida)
                quarto_encontrado.disponivel = False
                reservas.append(reserva)

                print(f">> Reserva realizada com sucesso! Valor total: R$ {reserva.valor_total:.2f}")

            # ------------------------------------------
            # OPÇÃO 4: LISTAGEM DE RESERVAS ATIVAS
            # ------------------------------------------
            elif opcao == "4":
                print("\n--- Reservas Ativas ---")
                if not reservas:
                    print("Nenhuma reserva registrada.")
                    continue
                for r in reservas:
                    print(
                        f"Cliente: {r.cliente.nome} | Quarto: {r.quarto.numero} | Período: {r.data_entrada.strftime('%d/%m/%Y')} até {r.data_saida.strftime('%d/%m/%Y')} | Total: R$ {r.valor_total:.2f}")

            # ------------------------------------------
            # OPÇÃO 5: CHECKOUT (LIBERAÇÃO DE QUARTO)
            # ------------------------------------------
            elif opcao == "5":
                print("\n--- Checkout (Liberar Quarto) ---")
                if not reservas:
                    print(">> Nenhuma reserva ativa para realizar checkout.")
                    continue

                num_quarto = int(input("Número do quarto para checkout: "))
                reserva_encontrada = next((r for r in reservas if r.quarto.numero == num_quarto), None)

                if not reserva_encontrada:
                    print(">> Erro: Nenhuma reserva ativa encontrada para este quarto.")
                    continue

                # Restaura a disponibilidade do quarto e remove a reserva ativa
                reserva_encontrada.quarto.disponivel = True
                reservas.remove(reserva_encontrada)
                print(f">> Checkout realizado com sucesso! O Quarto {num_quarto} agora está disponível.")

            # ------------------------------------------
            # OPÇÃO 6: SAIR DO SISTEMA
            # ------------------------------------------
            elif opcao == "6":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print(">> Opção inválida! Escolha um número de 1 a 6.")

        # ------------------------------------------
        # BLOCOS DE TRATAMENTO DE EXCEÇÕES GLOBAIS
        # ------------------------------------------
        except ValueError as e:
            print(f">> Erro de validação: {e}")
        except Exception as e:
            print(f">> Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    menu()