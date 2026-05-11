meta = float(input("Qual a porcentagem da meta atingida? "))

if meta >= 100:
    print("Excelente! Você bateu a meta com sucesso e ganhou um bônus! Continue assim!")
elif meta >= 80:
    print("Muito bom! Você chegou perto de bater a meta. Mantenha o foco que o próximo mês é seu!")
elif meta >= 50:
    print("Atenção: Seu desempenho foi regular. Vamos identificar o que pode melhorar para o próximo período.")
else:
    print("Alerta: O desempenho ficou abaixo do esperado. Procure seu gestor para traçar um plano de ação.")