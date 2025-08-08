# Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e
# escrever a média aritmética dessas notas lidas.

soma_notas = 0 
numero_alunos = int(input("informe a quantidade de alunos na turma: "))
for c in range (0, numero_alunos):
    nota = float(input(f"informe a nota do {c+1}° aluno: "))
    soma_notas += nota
media_turma = soma_notas / numero_alunos
print(media_turma)