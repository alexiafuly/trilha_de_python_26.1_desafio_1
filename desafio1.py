from IPython.core.formatters import format_display_data
# 1 - Entrada de dados e tipos

## Definindo as variáveis de entrada com uma restrição - estrição - Se o usuário inserir valores inválidos (negativos), o programa exibe uma mensagem de erro e para de executar.

orçamento = float(input("Digite o orçamento disponível para a viagem em reais: "))
if orçamento < 0:
     raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

##  try:
##    orçamento = float(input("Digite o orçamento disponível para a viagem em reais: "))
##    break
##  except TypeError:
##    print("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")


destino = str(input("Digite aqui o nome da cidade/país de destino da viagem: "))

custo_passagem = float(input("Digite o custo da passagem em reais: "))
while True:
  if custo_passagem >=0:
    break
  else:
    custo_passagem = input("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

custo_diario = float(input("Digite o custo diário de hospedagem em euros: "))
while True:
  if custo_diario >=0:
    break
  else:
    custo_diario = input("Ops, parece que você digitou um valor inválido! Digite um número positivo: ")

qtd_dias = int(input("Digite a quantidade de dias de duração da viagem: "))
while True:
  if qtd_dias >=0:
    break
  else:
    qtd_dias = input("Ops, parece que você digitou um valor inválido! Digite um número positivo e inteiro: ")


# 2 - Cálculos e lógica

## Conversão do custo diário de euros pra reais (1 EUR = 6.10 BRL)
custo_diario_BRL = custo_diario * 6.10

## Cálculo da hospedagem - multiplicação do custo diário (em reais) pela quantidade de dias
custo_hospedagem = custo_diario_BRL * qtd_dias

## Custo total da viagem - soma dos gastos com passagem e hospedagem em reais
custo_total = custo_passagem + custo_hospedagem

## Validação de orçamento -
if custo_total <= orçamento:
  Orçamento_possível = True
else:
  Orçamento_impossível = True

## Status final da viagem -
if custo_total < orçamento and qtd_dias > 0:
  viável = True
else:
  inviável = True

## Cálculo da diferença - quanto sobra ou quanto falta no orçamento para cobrir o custo total da viagem
diferença = orçamento - custo_total
if diferença < 0:
  falta = True
else:
  sobra = True

# 3 - Exibição de resultados

print(f"O custo total da hospedagem em reais é: {int(custo_hospedagem)} reais")

print(f"O custo total da viagem em reais é: {int(custo_total)} reais")

if custo_total <= orçamento:
  print("Orçamento possível")
else:
  print("Orçamento impossível")

if custo_total < orçamento and qtd_dias > 0:
  print("Status da viagem: viável.")
else:
 print("Status da viagem: inviável.")

if diferença < 0:
  print(f"Faltam {diferença} reais para cobrir os custos da viagem.")
else:
  print(f"Sobraram {int(diferença)} reais do orçamento disponível para a viagem.")


