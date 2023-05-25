
# 57035101-k
# 73229421-k
# 31800893-0
# 90803801-0
encendido = True
while encendido:
    while True:
        print("                              ")
        print("Bienvenidos al SuperRutificador")
        print("                              ")
        rut = input("Ingrese rut sin punto,guion ni DV _")  # captura de datos
        print(rut)
        serie = [2, 3, 4, 5, 6, 7, 2, 3]  # serie de datos a multiplicar

        # condicion de validacion rut
        if 6 < len(rut) < 9:
            rut_ = list(rut)  # convertir str de datos  en lista []
            rut_.reverse()
            for i in range(len(rut_)):
                rut_[i] = int(rut_[i])
                producto = list(map(lambda x, y: x*y, rut_, serie))
            sumatoria = sum(producto)
            residuo = sumatoria % 11
            dv = 11-residuo
            if dv == 10:
                dv = "k"

            elif dv == 11:
                dv = "0"

            else:
                dv = 11 - residuo

            print("                              ")
            print(f'para el rut {rut } el digito verificador es {dv}')

        else:
            print("                              ")
            print("formato de rut NO VALIDO")

    while True:
        print("                              ")
        respuesta = input("Desea ingresar otro rut S/N ")
        if respuesta.lower() == "s":
            encendido = True
            break

        elif respuesta.lower() == "n":
            print("                              ")
            print("Gracias por utilizar el SuperRutificador !!!")
            encendido = False
            break
        else:
            print("                              ")
            print("Por favor, ingresa una opcion valida.")
    break
