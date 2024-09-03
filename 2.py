string = "Exemplo de string para verificar a existência da letra 'a'."

contagem_a = string.count('a') + string.count('A')

if contagem_a > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {contagem_a} vezes na string.")
else:
    print("A letra 'a' (maiúscula ou minúscula) não aparece na string.")
