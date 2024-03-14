#GlenK
#14/3/2024
#Practice to generally get the feel of how this is going to be

import PySimpleGUI as sg
from food import Food

sg.theme('BlueMono')

#Setting foods
burger = Food(title='Burger', price=8.90, image=r'School\AT1\practicestuff\burger.png')
pizza = Food(title='Pizza', price=11.20, image=r'School\AT1\practicestuff\pizza.png')
chicken = Food(title='Chicken', price=12.30, image=r'School\AT1\practicestuff\chicken.png')
kimchi_stew = Food(title='Kimchi Stew', price=13.50, image=r'School\AT1\practicestuff\kimchistew.png')

#Setting the menu layout
menu_layout = [
    [
        sg.Image(burger.image), 
        sg.Column([
            [sg.Text(f'{burger.title} - ${"{:.2f}".format(burger.price)}')],
            [sg.Button('-'), sg.Text(f'{burger.amount}', key='burger_amount_textbox', size=(2, 1)), sg.Button('+')]
        ])
    ],
    [
        sg.Image(pizza.image), 
        sg.Column([
            [sg.Text(f'{pizza.title} - ${"{:.2f}".format(pizza.price)}')],
            [sg.Button('-'), sg.Text(f'{pizza.amount}', key='pizza_amount_textbox', size=(2, 1)), sg.Button('+')]
        ])
    ],
    [
        sg.Image(chicken.image), 
        sg.Column([
            [sg.Text(f'{chicken.title} - ${"{:.2f}".format(chicken.price)}')],
            [sg.Button('-'), sg.Text(f'{chicken.amount}', key='chicken_amount_textbox', size=(2, 1)), sg.Button('+')]
        ])
    ],
    [
        sg.Image(kimchi_stew.image), 
        sg.Column([
            [sg.Text(f'{kimchi_stew.title} - ${"{:.2f}".format(kimchi_stew.price)}')],
            [sg.Button('-'), sg.Text(f'{kimchi_stew.amount}', key='kimchi_stew_amount_textbox', size=(2, 1)), sg.Button('+')]
        ])
    ]
]

menu_window = sg.Window('MENU', layout=menu_layout, size=(1000, 600))

while True:
    event, values = menu_window.read()
    if event == sg.WIN_CLOSED:
        break

menu_window.close()