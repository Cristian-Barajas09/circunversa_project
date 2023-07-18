from view.Form import Form
from view.vista import Vista
from controller.controlador import Controlador
if __name__ == '__main__':
    control = Controlador()

    sesion = control.get_sesion()
    if len(sesion) > 0:
        user = control.obtener_usuario(sesion[0])
        Vista(user)
    else:
        Form()