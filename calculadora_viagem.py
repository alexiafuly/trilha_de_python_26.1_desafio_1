from IPython.core.formatters import format_display_data
# 1 - Entrada de dados e tipos

## Definindo as variáveis de entrada com uma restrição: se o usuário inserir valores inválidos (negativos), o programa exibe uma mensagem de erro e para de executar.

orçamento = float(input("Digite o orçamento disponível para a viagem em reais: "))
if orçamento < 0:
     raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

destino = str(input("Digite aqui o nome da cidade/país de destino da viagem: "))

custo_passagem = float(input("Digite o custo da passagem em reais: "))
if custo_passagem < 0:
     raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

custo_diario = float(input("Digite o custo diário de hospedagem em euros: "))
if custo_diario < 0:
     raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

qtd_dias = int(input("Digite a quantidade de dias de duração da viagem: "))
if qtd_dias < 0:
     raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")


# 2 - Cálculos e lógica

## Conversão do custo diário de euros pra reais (1 EUR = 6.10 BRL).
custo_diario_BRL = custo_diario * 6.10

## Cálculo da hospedagem - Multiplicação do custo diário (em reais) pela quantidade de dias.
custo_hospedagem = custo_diario_BRL * qtd_dias

## Custo total da viagem - Soma dos gastos com passagem e hospedagem em reais.
custo_total = custo_passagem + custo_hospedagem

## Validação de orçamento - Definindo o orçamento como possível se ele for igual ou maior que o custo total.
Orçamento_possível = ()
if custo_total <= orçamento:
  Orçamento_possível = True
else:
  Orçamento_possível = False

## Status final da viagem - Definindo a viagem como viável se o orçamento for igual ou maior que o custo total e a duração for maior que 0 dias.
viável = ()
if custo_total <= orçamento and qtd_dias > 0:
  viável = True
else:
  viável = False

## Cálculo da diferença - Definindo se vai faltar ou sobrar dinheiro no orçamento para cobrir o custo total da viagem.
diferença = orçamento - custo_total
falta = ()
if diferença < 0:
  falta = True
else:
  falta = False
  sobra = True

# 3 - Exibição de resultados - Printando o resultado dos cálculos utilizando f strings e condicionais.

print(f"O custo total da hospedagem em reais é: {round(custo_hospedagem,2)} reais")

print(f"O custo total da viagem em reais é: {round(custo_total,2)} reais")

if Orçamento_possível == True:
  print("Orçamento possível")
else:
  print("Orçamento impossível")

if viável == True:
  print("Status da viagem: viável.")
else:
 print("Status da viagem: inviável.")

if falta == True:
  print(f"Faltam {round(diferença,2)} reais para cobrir os custos da viagem.")
else:
  print(f"Sobraram {round(diferença,2)} reais do orçamento disponível para a viagem.")


