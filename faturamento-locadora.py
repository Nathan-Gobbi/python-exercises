estoque = int(input("Qual a quantidade de estoque: "))
valor_locação = float(input("Qual valor por locação: R$ "))


quantidade_de_videos_alugado = estoque//3 #// para não ter valor arredondado
faturamento_mensal = quantidade_de_videos_alugado * valor_locação
faturamento_ano =  faturamento_mensal * 12

videos_atrasados = quantidade_de_videos_alugado//10
multa_de_atraso = videos_atrasados * (valor_locação*0.10)

videos_estragados = estoque * 0.02
videos_reposicao = estoque // 10
estoque_final = estoque - videos_estragados + videos_reposicao

print(f"Seu faturamento anual será de R$ {faturamento_ano:.2f} ")
print(f"Valor arecadado com multas R$ {multa_de_atraso:.2f} ")
print(f"Previsão de estoque ao fim do ano {estoque_final:.0f}")