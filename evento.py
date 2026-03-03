workshop1 = {"Ana","Bruna","Cleuza","Dafne","Eelena","Caio"}
workshop2 = {"Alice","Brenda","Caio","Douglas","Eithor","Ana"}

participantes_a = set(workshop1)
participantes_b = set(workshop2)

print(f"Participantes do evento 1: {participantes_a}")
print(f"Participantes do evento 2: {participantes_b}")

todos_participantes = participantes_a.union(participantes_b)
print(f"Total de participantes: {todos_participantes}\n")
print(len(todos_participantes))

ambos_workshops = participantes_a.intersection(participantes_b)
print(f"Participantes nos dois worshops: {ambos_workshops}\n")

so_a = participantes_a.difference(participantes_b)
print(f"Apenas particpantes do Workshop 1: {so_a}")