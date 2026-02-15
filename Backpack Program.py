import time

backpack = {      'Food rations': 2,
                  'Acoustic guitar': 1,
                  'Paper planes': 2,}
running = True
while running:
    print('Which item would you like to use?')
    time.sleep(1)
    print('1. Food ration')
    print('2. Acoustic guitar')
    print('3. paper plane')
    time.sleep(1)
    selection1 = input('Select an option: 1, 2, 3, or q to quit.  ')
    time.sleep(1)
    if selection1 == '1':
        if backpack['Food rations'] > 0:
            backpack['Food rations'] -= 1
            print('You used a food ration.')
        else:
            print('You have no more food rations.')
    elif selection1 == '2':
        if backpack['Acoustic guitar'] > 0:
            backpack['Acoustic guitar'] -= 1
            print('You used your acoustic guitar, but broke a string.')
        else:
            print('You guitar is broken.')
    elif selection1 == '3':
        if backpack['Paper planes'] > 0:
            backpack['Paper planes'] -= 1
            print('You used a paper plane.')
        else:
            print('You have no more paper planes.')
    elif selection1 == 'q':
        print('Goodbye!')
        running = False
        break
    else:
        print('Invalid selection.')