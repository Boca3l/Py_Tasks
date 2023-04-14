import datetime
import pandas as pd
import os

caminho = 'dados/dados.csv'

def menu_def ():
    return int(input('Selecione a ação que deseja realizar?\n1 - Adicionar Tarefa\n2 - Deletar Tarefa\n3 - Alterar Status\n0 - Sair\n'))

def print_csv(db):
    db.to_csv(caminho,sep=';',index=False)

def first_row ():
    os.makedirs('dados')
    colunas = ['Tarefa','Inicio','Data_Final','Status']
    db = pd.DataFrame(columns=colunas)
    print(db)
    print_csv(db)

def show_db ():
    db = pd.read_csv(caminho,sep=';')

    if(db.empty):
        print('Base de Dados Vazia\n')
    else:
        print(db.head(),'\n')

def new_row ():
    tarefa = input('Informe a Tarefa: ')
    prazo = int(input('Informe o prazo previsto (em dias): '))
    hoje = datetime.date.today()
    data_final = hoje+datetime.timedelta(days=prazo)
    new_row = [tarefa,hoje,data_final,'Pendente']
    db = pd.read_csv(caminho,sep=';')
    db.loc[len(db)]= new_row
    print_csv(db)
    print('\n')

def delet_row():
    tarefa = int(input('Informe a Tarefa que deseja Excluir? '))
    db = pd.read_csv(caminho,sep=';')
    db = db.drop(tarefa)
    print_csv(db)
    show_db()

def update_row(row,col,value):
    db = pd.read_csv(caminho,sep=';')
    db.loc[[row],[col]] = value

    print_csv(db)
    show_db()

def update_status():
    tarefa = int(input('Informe a Tarefa: '))
    status = input('Informe o novo Status: ')
    print('\n')
    update_row(tarefa,'Status',status)

def update_Tarefa():
    tarefa = int(input('Informe a Tarefa: '))
    status = input('Informe o novo Status: ')
    print('\n')
    update_row(tarefa,'Status',status)

