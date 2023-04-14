import os
import assets

if not os.path.exists('dados'):
    assets.first_row()
    assets.show_db()
else:
    assets.show_db()

function = int(1)

while(function!=0):
    function = assets.menu_def()

    match(function):
        case 1:
            assets.new_row()
            assets.show_db()
            
        case 0:
            exit()

        case 2:
            assets.delet_row()
            assets.show_db()

        case 3:
            assets.update_status()
            assets.show_db()

        case _:
            print('Valor Inválido...')
