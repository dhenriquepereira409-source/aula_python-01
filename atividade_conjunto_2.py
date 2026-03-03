conjunto1 = {"laranja","ameixa","bolo","laranja","amora","sal"}
conjunto2 = {"feijão","bolo","macarrão","bolo","farinha","sal"}
conjunto3 = {"bolacha","biscoito","bolo","maça","pudim","sal"}
conjunto4 = {"amaciante","detergente","sal","bolo","pasta-de-dente","escova"}

pessoa_a = set(conjunto1)
pessoa_b = set(conjunto2)
pessoa_c = set(conjunto3)
pessoa_d = set(conjunto4)

print(f"Participantes do evento 1: {pessoa_a}")
print(f"Participantes do evento 2: {pessoa_b}")
print(f"Participantes do evento 1: {pessoa_c}")
print(f"Participantes do evento 2: {pessoa_d}")

ambos_conjuntos = conjunto1.intersection(pessoa_a,pessoa_b,pessoa_c,pessoa_d)
print(f"\nParticipantes nos dois conjuntos: {ambos_conjuntos}\n")

todas_pessoas = pessoa_a.union(pessoa_a,pessoa_b,pessoa_c,pessoa_d)
print(f"Total de pessoas: {todas_pessoas}\n")
print("O numero total de pessoas é: ")
print(len(todas_pessoas))