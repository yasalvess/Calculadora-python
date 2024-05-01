import flet as ft
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': "#000000", 'fundo': "#B4C3FD"},
    {'operador': '+-', 'fonte': "#000000", 'fundo': "#B4C3FD"},
    {'operador': '%', 'fonte': "#000000", 'fundo': "#B4C3FD"},
    {'operador': '/', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
    {'operador': '7', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '8', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '9', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '*', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
    {'operador': '4', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '5', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '6', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '-', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
    {'operador': '1', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '2', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '3', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '+', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
    {'operador': '0', 'fonte': "#3f51b5", 'fundo': "#B4C3FD"},
    {'operador': '.', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
    {'operador': '=', 'fonte': "#FFFFFF", 'fundo': "#3f51b5"},
]

def main(page: ft.Page):
    BG = '#100027' #cor roxo escuro
    DT = '#B4C3FD' #cor lilas
    LN = '#FFFFFF' #cor branco
    LN2 = "#000000" #cor preto
    BT = "#3f51b5" #cor indigo lighten 1
    
    page.bgcolor = BG
    page.window_resizable = False #par o usuário não redimensionar a tela
    page.window_width = 270
    page.window_height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color=LN, size=20)
    
    def calculate(operador, value_at):
        try:
            value = eval(value_at)
            
            if operador == '%':
                value /= 100
            elif operador == '+-':
                value = -value #inverte o valor
        except:
            return 'Error'
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')
    
    #função para lidar com a seleção de botões da calculadora
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ' '
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]
                
            value = value_at + value
            
            if value[-1] in ('=', '%', '+-'):
                value = calculate(operador = value[-1], value_at=value_at)
        result.value = value
        result.update()
    
    
    btn = [ft.Container(
        content=ft.Text(value = btn['operador'], color=btn['fonte']),
        alignment = ft.alignment.center,
        width = 50,
        height = 50,
        bgcolor = btn['fundo'],
        border_radius = 100,
        on_click = select
        )for btn in botoes]
    
    #configuração dos elementos de exibição do reultado e do teclado
    display = ft.Row( #criando uma linha
        width = 250, #para ficar exatamento do tamanho da janela
        controls=[result],
        alignment = 'end' #alinhado o result ao final da row
    )
    keyboard = ft.Row(
        width = 250,
        wrap = True,
        controls = btn,
        alignment= 'end'
    )
    page.add(display, keyboard)

ft.app(target = main)