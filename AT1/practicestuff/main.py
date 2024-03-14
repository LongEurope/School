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
all_foods = [burger, pizza, chicken, kimchi_stew]
all_foods_string = ['burger', 'pizza', 'chicken', 'kimchi_stew']

#Setting the menu layout
menu_layout = [
    [
        sg.Image(burger.image), 
        sg.Column([
            [sg.Text(f'{burger.title} - ${"{:.2f}".format(burger.price)}')],
            [sg.Button('-', key='burg-'), sg.Text(f'{burger.amount}', key='burger_amount_textbox', size=(2, 1)), sg.Button('+', key='burg+')]
        ])
    ],
    [
        sg.Image(pizza.image), 
        sg.Column([
            [sg.Text(f'{pizza.title} - ${"{:.2f}".format(pizza.price)}')],
            [sg.Button('-', key='pizz-'), sg.Text(f'{pizza.amount}', key='pizza_amount_textbox', size=(2, 1)), sg.Button('+', key='pizz+')]
        ])
    ],
    [
        sg.Image(chicken.image), 
        sg.Column([
            [sg.Text(f'{chicken.title} - ${"{:.2f}".format(chicken.price)}')],
            [sg.Button('-', key='chic-'), sg.Text(f'{chicken.amount}', key='chicken_amount_textbox', size=(2, 1)), sg.Button('+', key='chic+')]
        ])
    ],
    [
        sg.Image(kimchi_stew.image), 
        sg.Column([
            [sg.Text(f'{kimchi_stew.title} - ${"{:.2f}".format(kimchi_stew.price)}')],
            [sg.Button('-', key='kimc-'), sg.Text(f'{kimchi_stew.amount}', key='kimchi_stew_amount_textbox', size=(2, 1)), sg.Button('+', key='kimc+')]
        ])
    ],
    [
        sg.Button('RESET ORDER', pad=((700, 0),(100, 0))),
        sg.Button('CONFIRM ORDER', pad=((10, 0),(100, 0)))
    ]
]

#functions adding and minusing amounts of foods
def plus(food, strfood):
    if food.amount > 98:
        sg.popup('You cannot order more than 99', title='Error')
    else:
        food.amount += 1
        menu_window[f'{strfood}_amount_textbox'].update(food.amount)

def minus(food, strfood):
    if food.amount < 1:
        sg.popup('You cannot order less than 0', title='Error')
    else:
        food.amount -= 1
        menu_window[f'{strfood}_amount_textbox'].update(food.amount)

menu_window = sg.Window('MENU', layout=menu_layout, size=(1000, 600))

while True:
    event, values = menu_window.read()
    #If event is closed
    if event == sg.WIN_CLOSED:
        break
    #reset and confirm order stuff
    elif event == 'RESET ORDER':
        for food in all_foods:
            food.amount = 0
            for string in all_foods_string:
                menu_window[f'{string}_amount_textbox'].update(food.amount)
    elif event == 'CONFIRM ORDER':
        pass
    #Attaching functions to buttons
    elif event == 'burg+':
        plus(burger, 'burger')
    elif event == 'burg-':
        minus(burger, 'burger')
    elif event == 'pizz+':
        plus(pizza, 'pizza')
    elif event == 'pizz-':
        minus(pizza, 'pizza')
    elif event == 'chic+':
        plus(chicken, 'chicken')
    elif event == 'chic-':
        minus(chicken, 'chicken')
    elif event == 'kimc+':
        plus(kimchi_stew, 'kimchi_stew')
    elif event == 'kimc-':
        minus(kimchi_stew, 'kimchi_stew')

menu_window.close()