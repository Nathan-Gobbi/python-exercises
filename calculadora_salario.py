valor_hora = float(input("Digite o valor da hora trabalhada: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
percentual_inss = float(input("Digite o percentual de desconto do INSS: "))

salario_bruto = valor_hora * horas_trabalhadas
desconto_inss = salario_bruto * (percentual_inss / 100)
salario_liquido = salario_bruto - desconto_inss

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
# exercicios-python
