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
all_fields = ['Full Name I', 'Card Number I', 'Postcode I', 'Expiry Date I', 'Address I', 'CCV I']

#Setting and making the menu layout
def goto_menu_screen():
    global menu_window
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
            goto_order_screen()
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
        sg.Push(),
        sg.Button('RESET ORDER', pad=((0, 0), (100, 0))),
        sg.Button('CONFIRM ORDER', pad=((10, 0), (100, 0)))
    ]
]

#Setting and making order screen
def goto_order_screen():
    global ordered_foods
    ordered_foods = []
    for food in all_foods:
        if food.amount > 0:
            ordered_foods.append(food)
    order_layout = create_order_screen()

    order_window = sg.Window('ORDER', order_layout, size=(1000, 600))

    while True:
        event, values = order_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'BACK':
            order_window.close()
        elif event == 'CONFIRM ORDER':
            goto_payment_screen()

def create_order_screen():
    f_order_layout = []
    total_price = 0
    spacer_count = len(all_foods)
    for present_food in ordered_foods:
        price_for_food = float(present_food.price * present_food.amount)
        total_price += price_for_food
        spacer_count -= 1
        f_order_layout.append([sg.Text(f'{present_food.amount} x {present_food.title}', size=(15, 1), background_color='white'), sg.Text(f'${"{:.2f}".format(price_for_food)}', size=(10, 1), background_color='white')])
    f_order_layout.append([sg.Text('TOTAL', size=(15, 1), background_color='white'), sg.Text(f'${"{:.2f}".format(total_price)}', size=(10, 1), background_color='white')])
    for _ in range(spacer_count):
        f_order_layout.append([sg.Text('', size = (1, 1))])
    f_order_layout.append([sg.Text('', size=(1, 25))])
    f_order_layout.append([sg.Push(), sg.Button('BACK'), sg.Button('CONFIRM ORDER', pad=((10, 0), (0, 0)))])
    return f_order_layout
#Setting and making delivery information and payment screen:
def goto_payment_screen():
    payment_window = sg.Window('PAYMENT', layout=create_payment_screen(), size=(1000, 600))

    while True:
        event, values = payment_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'CANCEL':
            payment_window.close()
        elif event == 'CONFIRM PAYMENT':
            validation(payment_window)

def create_payment_screen():
    total_price = 0
    for present_food in ordered_foods:
        price_for_food = float(present_food.price * present_food.amount)
        total_price += price_for_food
    payment_layout = [
        [sg.Text('Please enter your details', font=('Helvetica', 30, 'normal'))],
        [sg.Column([
            [sg.Text('Full Name')],
            [sg.Multiline(key='Full Name I', size=(40, 5), background_color='white')],
            ]),
        sg.Column([
                [sg.Text('Card Number')],
                [sg.Multiline(key='Card Number I', size=(40, 5), background_color='white')]
        ])],
        [sg.Column([
            [sg.Text('Postcode')],
            [sg.Multiline(key='Postcode I', size=(40, 5), background_color='white')],
            ]),
        sg.Column([
                [sg.Text('Expiry Date')],
                [sg.Multiline(key='Expiry Date I', size=(40, 5), background_color='white')]
        ])],
        [sg.Column([
            [sg.Text('Address')],
            [sg.Multiline(key='Address I', size=(40, 5), background_color='white')],
            ]),
        sg.Column([
                [sg.Text('CCV')],
                [sg.Multiline(key='CCV I', size=(40, 5), background_color='white')]
        ])],
        [sg.Text('', size=(1, 6))],
        [sg.Push(), sg.Button('CANCEL'), sg.Button(f'PAY ${"{:.2f}".format(total_price)}', key='CONFIRM PAYMENT')]    
    ]
    return payment_layout

#Check if all the fields are correct:
def validation(win):
    invalid = False
    full_name = win['Full Name I'].get()
    card_number = win['Card Number I'].get()
    postcode = win['Postcode I'].get()
    expiry_date = win['Expiry Date I'].get()
    address = win['Address I'].get()
    ccv = win['CCV I'].get()

    check_full_name = ''
    for character in full_name:
        if character != ' ':
            check_full_name += character
    if not check_full_name.isalpha():
        print('Full name incorrect')
        invalid = True
    
    check_card_number = ''
    for digit in card_number:
        if digit != ' ':
            check_card_number += digit

    if not check_card_number.isdigit() or not len(check_card_number) == 16:
        print('Card number incorrect')
        invalid = True
    if not postcode.isdigit() or not len(postcode) == 4:
        print('Postcode incorrect')
        invalid = True
    if not expiry_date[0:2].isdigit() or not expiry_date[2] == '/' or not expiry_date[3:5].isdigit() or not len(expiry_date) == 5:
        print('Expiry Date incorrect')
        invalid = True
    if not address:
        print('Address incorrect')
        invalid = True
    if not ccv.isdigit() or not len(ccv) == 3:
        print('CCV incorrect')
        invalid = True
    
    if not invalid:
        print('Valid')

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

#Main
goto_menu_screen()