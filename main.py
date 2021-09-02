import funciones.crud as fun

# PREGUNTA#1 - Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
# megavatios de consumos para dicha ciudad en dicha planta

# PREGUNTA#2 - Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
# son los nombres de las plantas generadoras y el valor es el total megavatios que cada
# planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
# no debería aparecer en el nuevo diccionario

# PREGUNTA#3 - Solicite el nombre de una región al usuario y presente cuanto dinero ha recaudado la
# región Sierra

# PREGUNT#4 - Presentar el consumo total del mes ingresado

opc= 0
while opc!="5":
    print("\nEL SIGUIENTE PROGRAMA PERMITE: ")
    print("1. Presentar el total de megavatios de consumo de la ciudad que se ingrese en la planta ingresada")
    print("2. Presentar el total de megavatios dada por la planta respectiva a la ciudad ingresada")
    print("3. Presentar el dinero recaudado por región")
    print("4. Presentar el dinero generado por mes en las respectivas plantas")
    print("5. Terminar el programa")
    opc=input("Elija una opción: ")
    if opc=="1":
        print("")
        planta = input("Ingrese el nombre de la planta: ")
        planta = planta.lower()
        if planta == "coca codo sinclair":
            planta = "Coca Codo Sinclair"
            print("")
            ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad = ciudad.lower()
            contador_coca = fun.buscar_generador_Coca(ciudad)
            if contador_coca != None:
                ciudad=ciudad.capitalize()
                print("\nLa ciudad de",ciudad, "consume",contador_coca, "megavatios en la planta",planta)
            else:
                print("\nLa ciudad de",ciudad.capitalize(), "no pertenece a la planta", planta,".")
        elif planta == "sopladora":
            planta = "Sopladora"
            print("")
            ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad=ciudad.lower()
            contador_sopladora = fun.buscar_generador_Sopladora(ciudad)
            if contador_sopladora != None:
                ciudad=ciudad.capitalize()
                print("\nLa ciudad de",ciudad, "consume",contador_sopladora, "megavatios en la planta", planta)
            else:
                print("\nLa ciudad de",ciudad.capitalize(),"no pertenece a la planta",planta,".")
        else:
            print("\nNOMBRE DE PLANTA INCORRECTO")
    elif opc=="2":
        #print("\n2\n")
        print("")
        ciudad=input("Ingrese el nombre de la ciudad: ")
        ciudad=ciudad.lower()
        print()
        if (fun.buscar_ciudad(ciudad)!=None ):
            print("Ciudad: ",fun.buscar_ciudad(ciudad).capitalize())
            if (fun.buscar_generador_Sopladora(ciudad)!=None ):
                print('\nCompañia: Sopladora')
                print("Total de Voltios: ",fun.buscar_generador_Sopladora(ciudad),"\n")
            else:
                print("No existe relacion entre la ciudad de",ciudad.capitalize(),"y compañia Sopladora\n")
            if (fun.buscar_generador_Coca(ciudad)!=None ):
                print('Compañia: Coca Codo Sinclair')
                print("Total de Voltios: ",fun.buscar_generador_Coca(ciudad),"\n")
            else:
                print("No existe relacion entre la ciudad de",ciudad.capitalize(),"y compañia Coca Codo Sinclair\n")
        else:
            print("No existe la ciudad",ciudad.capitalize(),"dentro del diccionario de regiones. \n")            
    elif opc=="3":
        r="0"
        while r!="4":
            print("\nSeleccione la región a consultar: ")
            print("1. Costa")
            print("2. Sierra")
            print("3. Oriente")
            print("4. Regresar")
            r=input("Elija una opción: ")
            if r=="1":
                print("\nEl valor consumo de la región Costa es de $",fun.dinero_region(r))
            elif r=="2":
                print("\nEl valor de consumo de la región Sierra es de $",fun.dinero_region(r))
            elif r=="3":
                print("\nEl valor de consumo en la región Oriente es de: $",fun.dinero_region(r))
            elif r=="4":
                r="4"
            else:
                print("\nOPCIÓN INCORRECTA") 
    elif opc=="4":
        mc=0
        while mc==0:
            print("")
            print("Ingrese un valor del 1-12, los cuales representan los meses del año: ")
            mes=input("Ingrese el número del mes a consultar: ")
            if mes in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                inf=fun.consumo_mensual(mes)
                print("\nLos valores de consumo del mes de",inf[0],"son:")
                print("\nCoca Codo Sinclair: $",inf[1])
                print("Sopladora: $",inf[2])
                print("\nTOTAL: $", inf[3])
                mc=1
            else:
                print("\nVALOR FUERA DEL RANGO ESTABLECIDO")
    elif opc=="5":
        print("\nFIN DEL PROGRAMA \n")
        opc="5"
    else:
        print("\nOPCIÓN INCORRECTA")
