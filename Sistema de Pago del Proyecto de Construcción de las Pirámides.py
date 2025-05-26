#Programa para pagos de la construcción de la Pirámide
#Paso 1: Impromir el mensaje de Bienvenida
print("Bienvenido/a al programa de pagos PIRAMIPAGOS")
print("Para continuar, ingrese los datos solicitados a continuación")
#Paso 2: Definir variables / Paso 4: Pago Total / Paso 7: Ciclo While para calcular el pago de varios trabajadores hasta que el usuario escriba "salir"
while True:
    Nombre = input("Nombre y apellido o digite salir para finalizar:")
    if Nombre.lower() == "salir":
        print("Gracias por visitar Piramipago, vuelva pronto!!!")
        break
    Horas_trabajadas_semana = int(input("Horas trabajadas en la semana:"))
    Numero_de_veces_que_llegó_tarde = int(input("¿Cuántas veces llegó tarde esta semana?:"))
    Tarifa_fija_por_hora = 15000
    Horas_de_jornada_semanal_fijo= 40 
    Total_horas_extras = Horas_trabajadas_semana-Horas_de_jornada_semanal_fijo
    Tarifa_hora_extras = Tarifa_fija_por_hora*1.2 
    Pago_total_horas_extras = Total_horas_extras*Tarifa_hora_extras
    Sueldo_bruto= Tarifa_fija_por_hora*Horas_de_jornada_semanal_fijo+Pago_total_horas_extras
    #Paso 3: Horas Extras 
    if Horas_trabajadas_semana > 40:
        print("Posee Horas extras, por lo tanto el pago por horas extras es de: ", Pago_total_horas_extras)
        print("Su sueldo bruto semanal es de $", Sueldo_bruto)
    elif Horas_trabajadas_semana==40:
        print("Usted no posee Horas extras")
        print("Su sueldo bruto semanal es de $", Sueldo_bruto)
#Paso 5: Bonificación
    if Sueldo_bruto>600000:
        print("Adicionalmente se le asignará un bono de $50000, siendo su sueldo total de $:",Sueldo_bruto+50000)
    else:
        print("Su sueldo total es de $", Sueldo_bruto)
#Paso 6: Descuento por tardanza
    if Numero_de_veces_que_llegó_tarde>=3:
        print("Se realiza un descuento por tardanza, quedándo su sueldo semanal en $:", Sueldo_bruto-Sueldo_bruto*0.05)
    else:
        print("No se realiza descuento por tardanza,quedándo su sueldo semanal en $", Sueldo_bruto)
    


