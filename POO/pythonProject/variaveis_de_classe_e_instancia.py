class Estudante:
    escola = 'Miskatonic'

    def __init__(self, nome: str, matricula: int):
        self.nome: str = nome
        self.matricula: int = matricula

    def __str__(self) -> str:
        return f'Aluno(a): {self.nome} | escola: {self.escola}, matrícula: {self.matricula}'


def mostrar_alunos(*alunos):
    for aluno in alunos:
        print(aluno)


gui = Estudante('Guilherme', 1)
mari = Estudante('Mariana', 2)
mostrar_alunos(gui, mari)

gui.matricula = 3
mostrar_alunos(gui, mari)

Estudante.escola = 'EJA'
gui.escola = 'EJA I'

guts = Estudante('Guts', 4)
mostrar_alunos(gui, mari, guts)