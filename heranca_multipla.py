class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


""" Quando olhamos a classe Junior ele tem acesso apenas a classe alura, ou seja, ele só pode acessar o atributos
daquela classe, porém podemos acessar a classe funcionario que é heranã da classe alura"""
jose = Junior()
jose.mostrar_tarefas()
"""Já o carlos é pleno e pode ter acesso as duas classes, tanto a Alura quando a Caelum e de tabela a classe 
Funcionarios, essa é a projeção de herança multipla, ou seja, posso reveber mais de uma herança."""