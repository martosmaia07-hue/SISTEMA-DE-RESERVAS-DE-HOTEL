from datetime import datetime

# ==========================================
# CLASSE: Cliente
# Representa o cliente do hotel
# ==========================================
class Cliente:
    def __init__(self, nome, documento, contato):
        self.nome = nome          # Nome completo do cliente
        self.documento = documento  # CPF formatado
        self.contato = contato    # Telefone formatado

    def __str__(self):
        # Representação textual amigável do objeto Cliente
        return f"Cliente: {self.nome} | Documento: {self.documento} | Contato: {self.contato}"


# ==========================================
# CLASSE: Quarto (Classe Base / Superclasse)
# Representa um quarto padrão do hotel
# ==========================================
class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero              # Número identificador do quarto
        self.tipo = tipo                  # Tipo de quarto (ex: Solteiro, Casal)
        self.preco_diaria = preco_diaria  # Valor da diária base
        self.disponivel = True            # Status inicial: disponível

    def calcular_valor(self, dias):
        """Calcula o valor base da estadia com base nos dias."""
        return dias * self.preco_diaria


# ==========================================
# CLASSE: QuartoLuxo (Subclasse / Herança e Polimorfismo)
# Herda de Quarto e sobrescreve o cálculo da diária
# ==========================================
class QuartoLuxo(Quarto):
    """Exemplo de Herança e Polimorfismo: QuartoLuxo herda de Quarto e altera o cálculo da diária."""
    def __init__(self, numero, preco_diaria):
        # Chama o construtor da classe pai fixando o tipo como "Luxo"
        super().__init__(numero, "Luxo", preco_diaria)

    def calcular_valor(self, dias):
        """Polimorfismo: sobrescreve o cálculo para acrescentar taxa de serviço de 15%."""
        valor_base = super().calcular_valor(dias)
        return valor_base * 1.15


# ==========================================
# CLASSE: Reserva
# Gerencia a associação entre Cliente e Quarto, datas e valores
# ==========================================
class Reserva:
    def __init__(self, cliente, quarto, data_entrada, data_saida):
        self.cliente = cliente
        self.quarto = quarto
        
        # Conversão de strings para objetos datetime
        self.data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y")
        self.data_saida = datetime.strptime(data_saida, "%d/%m/%Y")
        
        # Cálculo da quantidade de dias da estadia
        self.dias = (self.data_saida - self.data_entrada).days
        
        # Validação crítica do período de hospedagem
        if self.dias <= 0:
            raise ValueError("A data de saída deve ser estritamente posterior à data de entrada.")
        
        # Polimorfismo aplicado: chama o método calcular_valor correspondente ao tipo de quarto
        self.valor_total = quarto.calcular_valor(self.dias)