treinos = ["peito", "costas", "pernas", "ombro", "braços"]

# O primeiro treino da semana está no índice 0
print("Primeiro treino:", treinos[0])

# Mostrando todos os treinos
print("\nTreinos da semana:")
for treino in treinos:
    print("-", treino)

# Adicionando cardio no final
treinos.append("cardio")
print("\nLista atualizada com cardio:", treinos)

# Removendo pernas (já treinado)
treinos.remove("pernas")
print("Lista atualizada sem pernas:", treinos)