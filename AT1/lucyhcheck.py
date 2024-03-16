import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [
    [
        sg.Push(), sg.Button('View Full Menu'), sg.Push()
    ],
    [
        sg.Column([
            [sg.Button('Mains')],
            [sg.Button('Sides')],
            [sg.Button('Drinks')],
            [sg.Button('Extras')]
        ]),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Button('Your cart')
    ],
    [
        sg.Text('', size=(6, 1)),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Column([
            [sg.Image(r'School\AT1\practicestuff\pizza.png')],
            [sg.Text('Item 1')]
        ]),
        sg.Column([
            [sg.Text('Total cost: $XX XX')],
            [sg.Button('Purchase')]
        ])
    ]
]

window = sg.Window('Hi Lucy', layout, size =(600, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()