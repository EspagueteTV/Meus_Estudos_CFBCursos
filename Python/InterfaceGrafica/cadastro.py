from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit') #Escolher Tema
layout = [  #Criar os elementos de cada linha
    [sg.Text('Usuário'), sg.Input(key = 'usuario')],
    [sg.Text('Senha'), sg.Input(key = 'senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]


#Janela
janela = sg.Window('Tela de Login', layout) #Criar uma janela, o 1º Parametro é o seu nome, e o segundo o seu layout a ser utilizaaddo


#Ler os Eventos
while True:
    eventos, valores = janela.read()   #Ler informações da Janela

    if eventos == sg.WINDOW_CLOSED:     #Se o usuário fechar a Janela
        break

    if eventos == 'Entrar':     #Verificar os dados informados elo usuário
        if valores['usuario'] == 'Gabriel' and valores['senha'] == '1234':
            print('Bem vindo')


