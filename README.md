# 🏨 Sistema de Reservas de Hotel em Python

Este projeto foi desenvolvido em Python aplicando os paradigmas de programação estudados na disciplina, nomeadamente **programação procedural** e **orientada a objetos**.

---

## 🚀 Funcionalidades do Sistema

O sistema implementa as seguintes funcionalidades:
- **Cadastro de clientes**: Registo de nome, documento (CPF formatado com máscara) e contacto telefónico.
- **Cadastro de quartos e tipos de acomodação**: Quartos standard (solteiro e casal) e quartos de luxo, com controlo dinâmico de disponibilidade.
- **Realização de reservas**: Validação rigorosa de datas (impede datas passadas e garante que a data de saída seja estritamente posterior à de entrada) e verificação de disponibilidade do quarto.
- **Listagem de quartos**: Visualização do número, tipo, preço da diária e estado atual (disponível ou ocupado).
- **Listagem de reservas ativas**: Monitorização de clientes, quartos associados, período de estadia e valor total calculado.
- **Realização de Checkout**: Libertação de quartos ocupados e remoção da respetiva reserva ativa.

---

## 🛠️ Requisitos Técnicos Atendidos (Paradigmas Aplicados)

* **Estruturas de decisão e repetição**: Aplicadas no ciclo principal do menu (`while True`), nas estruturas condicionais (`if/elif/else`), na validação de datas (`while True` com blocos `try-except` na função `obter_data_valida`), e na filtragem/busca de elementos em listas com expressões geradoras (`next()`).
* **Subprogramas (funções)**: Funções auxiliares modularizadas no ficheiro `main.py` (`formatar_cpf`, `formatar_telefone`, `obter_data_valida`, `menu`) e métodos de instância definidos nas classes em `modelos.py` (`calcular_valor`, `__str__`).
* **Biblioteca(s) utilizada(s)**: 
  * `re`: Utilizada para limpeza e aplicação de máscaras em CPFs e números de telefone através de expressões regulares.
  * `datetime`: Usada para gerir datas, validar restrições temporais e calcular a quantidade exata de dias de estadia.
* **Tratamento de exceções**: Tratamento robusto de `ValueError` e exceções genéricas `Exception` no fluxo de interação do utilizador no menu principal (`main.py`), além de validações críticas que lançam `ValueError` caso a estadia seja inválida na classe `Reserva`.
* **Classes, atributos e métodos** (organizadas em `modelos.py`):
  * `Cliente`: atributos `nome`, `documento`, `contato` e método `__str__`.
  * `Quarto`: atributos `numero`, `tipo`, `preco_diaria`, `disponivel` e método `calcular_valor`.
  * `QuartoLuxo`: subclasse de `Quarto`.
  * `Reserva`: atributos `cliente`, `quarto`, `data_entrada`, `data_saida`, `dias`, `valor_total`.
* **Herança e polimorfismo**: Aplicados na criação da classe `QuartoLuxo`, que herda de `Quarto` (Herança) e sobrescreve o método `calcular_valor` para acrescentar uma taxa de serviço de 15% (Polimorfismo). A classe `Reserva` aplica polimorfismo ao invocar `quarto.calcular_valor(self.dias)`.

---

## 📁 Estrutura do Código

O código-fonte está organizado da seguinte forma:

```text
├── main.py       # Ponto de entrada do programa, menu principal e funções auxiliares
└── modelos.py    # Módulo com as classes do sistema (Cliente, Quarto, QuartoLuxo, Reserva)
```

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado na sua máquina.
2. Clone este repositório ou descarregue os ficheiros `main.py` e `modelos.py` para a mesma pasta.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python main.py
   ```

---

## 💡 Considerações Finais
O desenvolvimento deste projeto permitiu consolidar de forma prática os conceitos fundamentais da programação procedural e orientada a objetos em Python. As principais dificuldades persentiram-se com a validação do código e uma forma definitiva de adicionar uma formatação automática nos cadastros. Com melhorias futuras, aponta-se a implementação de persistência de dados e a criação de uma interface gráfica ou web.
---

## 🔗 Referências
* [Vídeo de Referência](https://www.youtube.com/watch?v=Rpe7TfSIqTE)
* [Repositório Base 1](https://github.com/markdevs/sys-hotel)
* [Repositório Base 2](https://github.com/marisarinho/hotel-reservation)
* [Repositório Base 3](https://github.com/brunocotto/sistema-reserva-hotel)
