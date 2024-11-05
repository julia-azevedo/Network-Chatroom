import PySimpleGUI as sg
import socket
import threading
import time

def get_nickname():
    layout = [[sg.Text('Enter username')],
    [sg.Input(key='-NICKNAME-')],
    [sg.Button('OK')]]

    window = sg.Window('Login', layout)

    nickname = ''
    while True:
        event, values = window.read()
        if event in (None, 'OK'):
            nickname = values['-NICKNAME-']
            break

    window.close()

    return nickname

